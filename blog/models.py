from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('editor', 'Editor'), 
        ('author', 'Author'),
        ('subscriber', 'Subscriber')
    ]
    
    id = models.CharField(max_length=36, primary_key=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='subscriber')
    full_name = models.CharField(max_length=200, blank=True, null=True)
    avatar_url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_profiles'

    def __str__(self):
        return self.full_name or f"User {self.id}"


class ArticleCategories(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.CharField(max_length=36, blank=True, null=True) 
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=20, default='#000000')
    sort_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name


class Authors(models.Model):
    ROLE_CHOICES = [
        ('author', 'Author'),
        ('admin', 'Admin'),
        ('editor', 'Editor')
    ]
    
    id = models.CharField(max_length=36, primary_key=True)
    user_id = models.CharField(max_length=36, blank=True, null=True)
    email = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    avatar = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='author')
    social_links = models.JSONField(default=dict, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'authors'

    def __str__(self):
        return self.name or self.email


class Tags(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tags'

    def __str__(self):
        return self.name


class ArticleLists(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived')
    ]
    
    id = models.CharField(max_length=36, primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    content = models.TextField(blank=True, null=True)
    excerpt = models.TextField(blank=True, null=True)
    featured_image = models.TextField(blank=True, null=True)
    
    # Foreign Key relationships (better practice)
    category = models.ForeignKey(ArticleCategories, on_delete=models.CASCADE, db_column='category_id')
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, db_column='author_id')
    
    published_at = models.DateTimeField(blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    is_featured = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    reading_time = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'articles'

    def __str__(self):
        return self.title


class ArticleTags(models.Model):
    article = models.ForeignKey(ArticleLists, on_delete=models.CASCADE, db_column='article_id', primary_key=True)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE, db_column='tag_id')

    class Meta:
        db_table = 'article_tags'
        unique_together = ('article', 'tag')

    def __str__(self):
        return f"{self.article.title} - {self.tag.name}"


class ArticleImages(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(ArticleLists, on_delete=models.CASCADE, related_name='images', db_column='article_id')
    image_url = models.TextField()
    alt_text = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'article_images'
    
    def __str__(self):
        return f"Image for {self.article.title}" if self.article else "Image without article"
