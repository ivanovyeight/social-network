from rest_framework import serializers
from .models import Image

from urllib import request

from django.core.files.base import ContentFile

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['url', 'title', 'description']


    def update(self, image, validated_data):
        image.url = validated_data.get('url', image.url)
        image.title = validated_data.get('title', image.title)
        image.description = validated_data.get('description', image.description)
        image.user = validated_data.get('user', image.user)
