from rest_framework import serializers
from models import Fruit

class FruitSerializer(serializers.ModelSerializer):
	slug = serializers.ReadOnlyField(source='slug.category')

	class Meta:
		model = Fruit
		fields = ('id', 'title', 'kinds' 'slug', 'content', 'price')
