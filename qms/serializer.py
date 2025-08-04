from rest_framework import serializers
from .models import QueueItem, QueueUser

class QueueUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueueUser
        fields = ['id', 'email', 'name', 'created_at', 'phone_number', 'last_updated']
        read_only_fields = ['created_at', 'last_updated']

class QueueItemSerializer(serializers.ModelSerializer):
    user = QueueUserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        source='user', queryset=QueueUser.objects.all(), write_only=True
    )
    # user = serializers.PrimaryKeyRelatedField(queryset=QueueUser.objects.all())

    class Meta:
        model = QueueItem
        fields = ['id', 'user', 'user_id', 'queue_position', 'description', 'status', 'estimated_wait_time', 'registered_at', 'start_time', 'end_time', 'created_at']
        read_only_fields = ['created_at']