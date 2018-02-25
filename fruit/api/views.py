from rest_framework import generics
from ..models import Fruit
from .serializers import FruitSerializer

class FruitListView(generics.ListAPIView):
	queryset = Fruit.objects.all()
	serializer_class = FruitSerializer

class FruitDetailView(generics.RetrieveAPIView):
	queryset = Fruit.objects.all()
	serializer_class = FruitSerializer
	