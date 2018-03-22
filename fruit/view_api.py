from serializer import FruitSerializer, ActivitySerializer
from rest_framework import generics, mixins, views
from rest_framework.pagination import LimitOffsetPagination
from models import Fruit, Activity
from rest_framework import status
from rest_framework.response import Response

class FruitList(generics.ListCreateAPIView, mixins.CreateModelMixin):
    queryset= Fruit.objects.all()
    serializer_class = FruitSerializer
    pagination_class = LimitOffsetPagination

class FruitDetail(views.APIView):
    queryset= Fruit.objects.all()
    serializer_class = FruitSerializer
    pagination_class = LimitOffsetPagination

    def get_object(self, id):
        try:
            return Fruit.objects.get(id=id)
        except Fruit.DoesNotExist:
            raise status.HTTP_404_NOTFOUND

    def get(self, request, id):
        fruit = self.get_object(id)
        serializer = FruitSerializer(fruit)
        return Response(serializer.data)

class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    pagination_class = LimitOffsetPagination
