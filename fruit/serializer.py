from rest_framework import serializers
from models import Fruit, Activity
from taggit.managers import TaggableManager
from taggit.models import Tag

class ActivitySerializer(serializers.ModelSerializer):
    image_position = serializers.CharField(source='full_image', required=False, read_only=True)
    fruits_in_activity = serializers.StringRelatedField(
            many=True,
            read_only=True)

    class Meta:
        model = Activity
        fields = ('id', 'category', 'image_position', 'fruits_in_activity')

    def create(self, validated_data):
        img = validated_data['img']
        
    def update(self, instance, validated_data):
        from django.core.files.base import ContentFile
        instance.category = validated_data['category']
        if validated_data.get('img', None):
            instance.image = ContentFile(validated_data['img'])
        instance.save()
        return instance

class FruitDeSerializer(serializers.ModelSerializer):
    kinds = serializers.CharField(required=False, write_only=True)
    slug = serializers.IntegerField(required=False, write_only=True)

    class Meta:
        model = Fruit
        fields = ('kinds','slug','title','content','price','detail')
    
    def validate_slug(self, value):
        try:
            Activity.objects.get(id=value)
        except Activity.DoesNotExist:
            raise serializers.ValidationError("slug id does not match any exists objects")
        return value

    def create(self, validated_data):
        img = validated_data['img']
        if validated_data.get("slug", False):
            slug = Activity.objects.get(id=validated_data['slug'])
        fruit = Fruit.objects.create(
                title=validated_data['title'],
                slug=slug,
                image_icon=img,
                content=validated_data['content'],
                detail=validated_data['detail'],
                price=validated_data['price'])
        fruit.kinds.add(validated_data['kinds_'])
        return fruit

    def update(self, instance, validated_data):
        if validated_data.get('slug', False):
            slug = Activity.objects.get(id=validated_data['slug'])
            instance.slug = slug
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.detail = validated_data.get('detail', instance.detail)
        instance.price = validated_data.get('price', instance.price)
        if validated_data.get("kinds_", None):
            instance.kinds.clear()
            instance.kinds.add(validated_data.get('kinds_'))
        instance.save()
        return instance

class FruitSerializer(serializers.ModelSerializer):
    kinds = serializers.CharField(source="tag_name")
    image_position = serializers.CharField(source='full_image_icon')
    image_content = serializers.CharField(source='full_image_content1')
    slug = ActivitySerializer(required=False)

    class Meta:
        model = Fruit
        fields = ('id', 'title', 'kinds', 'slug', 'image_position', 'content', 'price', 'image_content', 'detail')

    def validated_image_position(self, value):
        from os.path import exists
        if not exists(value):
            raise serializers.ValidationError("image_position path has no file")
        return value

    def create(self, validated_data):
        try:
            activity = Activity.objects.get(category=validated_data.slug['category'])
        except Activity.DoesNotExist:
            return 
        fruit=Fruit.object.create(
                title=validated_data.title, 
                content=validated_data.content,
                price=validated_data.price,
                detail=validated_data.detail)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
