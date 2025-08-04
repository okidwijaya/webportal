from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

passowrd_validator = RegexValidator(regex=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', message='Password must be at least 8 characters long and contain both letters and numbers.')

class user(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=100)
    # password = models.CharField(max_length=128)
    password = models.CharField(max_length=128, validators=[passowrd_validator])
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"id: {self.id}-user: {self.email}-Phone Number: {self.phone_number}"

class QueueUser(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"id: {self.id}-user: {self.email}-Phone Number: {self.phone_number}"
    
class QueueItem(models.Model):
    user = models.ForeignKey(QueueUser, on_delete=models.CASCADE, related_name='items')
    queue_position = models.IntegerField()
    description = models.TextField()
    status = models.CharField(max_length=20, default='pending')
    estimated_wait_time = models.IntegerField(help_text="Estimated wait time in minutes")
    registered_at = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.name}(id: {self.user.id}): {self.description} (Posisi: {self.queue_position}(item_id: {self.id}), Status: {self.status})"

