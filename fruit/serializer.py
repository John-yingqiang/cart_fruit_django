from rest_framework import serializers
from models import Fruit
from taggit.managers import TaggableManager
from taggit.models import Tag
from django.shortcuts import get_object_or_404

class FruitSerializer(serializers.ModelSerializer):
    kinds_ = serializers.CharField(source="tag_name")
    image_url = serializers.CharField(source='image_icon.url')

    class Meta:
        model = Fruit
        fields = ('title', 'title', 'kinds_', 'image_url', 'content', 'price')
    
    def create(self, validated_data):
        try:
            tag = get_object_or_404(Tag, name=validated_data.kinds)
        except Tag.DoesNotExist:            
            tag = TaggableManager

