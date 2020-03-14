from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        # Model in models.py
        model = Post
        fields = ('title', 'custom_id', 'owner', 'category', 'publish_date', 'last_published')
