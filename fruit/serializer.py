from rest_framework import serializers
from models import Fruit, Activity
from taggit.managers import TaggableManager


class IFruitSerializer(serializers.ModelSerializer):
    kinds_ = serializers.CharField(source="tag_name")
    image_position = serializers.CharField(source='full_image_icon')
    image_content = serializers.CharField(source='full_image_content1')

    class Meta:
        model = Fruit
        fields = ('title', 'kinds_', 'image_position', 'content', 'price', 'image_content', 'detail')

class ActivitySerializer(serializers.ModelSerializer):
    image_position = serializers.CharField(source='full_image')
    fruits_in_activity = serializers.StringRelatedField(
            many=True,
            read_only=True)

    class Meta:
        model = Activity
        fields = ('id', 'category', 'image_position', 'fruits_in_activity')

class FruitSerializer(serializers.ModelSerializer):
    kinds_ = serializers.CharField(source="tag_name")
    image_position = serializers.CharField(source='full_image_icon')
    image_content = serializers.CharField(source='full_image_content1')
    slug = ActivitySerializer()

    class Meta:
        model = Fruit
        fields = ('id', 'title', 'kinds_', 'slug', 'image_position', 'content', 'price', 'image_content', 'detail')
    
    def create(self, validated_data):
        fruit=Fruit.objects.create(
                title=validated_data.title, 
                content=validated_data.content,
                price=validated_data.price,
                detail=validated_data.detail)








