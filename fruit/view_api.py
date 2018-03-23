# -*- coding: utf-8 -*-
from serializer import FruitSerializer, ActivitySerializer
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from models import Fruit, Activity
from rest_framework import status
from rest_framework.response import Response
from common.return_format import JsonResponse


class FruitList(APIView):
    
    def get(self, request, format=None):
        
        fruits = Fruit.objects.all()
        serializer = FruitSerializer(fruits, many=True)
        return JsonResponse(serializer.data, code=200, desc=u'水果列表')        
   
    def post(self, request, format=None):
        serializer = FruitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

class FruitDetail(APIView):
    queryset= Fruit.objects.all()
    serializer_class = FruitSerializer

    def get_object(self, id):
        try:
            return Fruit.objects.get(id=id)
        except Fruit.DoesNotExist:
            raise status.HTTP_404_NOTFOUND

    def get(self, request, id):
        fruit = self.get_object(id)
        serializer = FruitSerializer(fruit)
        return Response(serializer.data)

class ActivityList(APIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
