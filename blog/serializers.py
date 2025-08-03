from rest_framework import serializers
import requests

from .models import (
    UserProfile, ArticleCategories, Authors, Tags,
    ArticleLists, ArticleTags, ArticleImages
)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class ArticleCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategories
        fields = '__all__'


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'
        
class ArticleImagesSerializer(serializers.ModelSerializer):
    image_file = serializers.ImageField(write_only=True, required=True)

    class Meta:
        model = ArticleImages
        fields = ['id', 'article', 'alt_text', 'image_url', 'image_file', 'created_at']
        read_only_fields = ['image_url', 'created_at']

    def create(self, validated_data):
        image_file = validated_data.pop('image_file')
        article = validated_data.get('article')

        files = {
            'file': (image_file.name, image_file.read(), image_file.content_type)
        }

        response = requests.post("https://cloudsand.my.id/upload_image/upload.php", files=files)

        if response.status_code != 200:
            raise serializers.ValidationError("Gagal mengupload gambar ke server.")

        image_url = response.json().get("url")
        if not image_url:
            raise serializers.ValidationError("Respons tidak valid dari server upload.")

        return ArticleImages.objects.create(
            article=article,
            alt_text=validated_data.get('alt_text', ''),
            image_url=image_url
        )

# class ArticleImagesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ArticleImages
#         fields = '__all__'


class ArticleTagsSerializer(serializers.ModelSerializer):
    tag = TagsSerializer(read_only=True)
    
    class Meta:
        model = ArticleTags
        fields = ['tag']


class ArticleListsSerializer(serializers.ModelSerializer):
    category = ArticleCategoriesSerializer(read_only=True)
    author = AuthorsSerializer(read_only=True)
    images = ArticleImagesSerializer(many=True, read_only=True)
    tags = serializers.SerializerMethodField()

    class Meta:
        model = ArticleLists
        fields = '__all__'

    def get_tags(self, obj):
        tags = ArticleTags.objects.filter(article=obj)
        return ArticleTagsSerializer(tags, many=True).data
