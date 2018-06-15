# -*- coding: utf-8 -*-
from serializer import FruitDeSerializer, FruitSerializer, ActivitySerializer, TagSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from models import Fruit, Activity
from taggit.models import Tag
from rest_framework import status
from rest_framework.response import Response
from common.return_format import JsonResponse
from urllib import unquote

@api_view()
def tag_list(request):
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return JsonResponse(serializer.data, code=200, desc=u'标签列表')


class FruitList(APIView):
    
    def get(self, request, format=None):
        query_param = request.query_params
        
        for key, value in query_param.items():
            print "key:{}, value:{}".format(key, unquote(value).decode('utf-8'))

        try:
            if not query_param:
                fruits = Fruit.objects.all()

            elif "order_by" in query_param:
                fruits = Fruit.objects.order_by(query_param.get('order_by'))

            else:
                fruits = Fruit.objects.filter(**query_param.dict())
        except Exception as e:
            print e

        serializer = FruitSerializer(fruits, many=True)
        return JsonResponse(serializer.data, code=200, desc=u'水果列表')        
   
    def post(self, request, format=None):
        serializer = FruitDeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, code=403, desc=u'错误信息')


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
        
        return JsonResponse((serializer.data,), code=200, desc=u'水果详情')

    def put(self, request, id):
        fruit = self.get_object(id)
        serializer = FruitDeSerializer(fruit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            fruit = self.get_object(id)
            serializer = FruitSerializer(fruit)
            return JsonResponse((serializer.data,), code=201, desc=u'详情页更新成功')
        else:
            return JsonResponse(serializer.errors, code=404, desc=u'数据错误')

class ActivityList(APIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer        

    def get(self, request, format=None):
        activitys = Activity.objects.all()
        serializer = ActivitySerializer(activitys, many=True)
        return JsonResponse(serializer.data, code=200, desc=u'活动列表')        
   
    def post(self, request, format=None):
        serializer = FruitDeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse((serializer.data,), code=201, desc=u'详情页更新成功')
        else:
            return JsonResponse(serializer.errors, code=403, desc=u'错误信息')

class ActivityDetail(APIView):
    
    def get_object(self, id):
        try:
            return Activity.objects.get(id=id)
        except Activity.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    
    def get(self, request, id):
        activity = self.get_object(id)
        serializer = ActivitySerializer(activity)
        return JsonResponse((serializer.data,), code=201, desc=u'活动列表')

    def put(self, request, id):
        activity = self.get_object(id)
        serializer = ActivitySerializer(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # fruit = self.get_object(id)
            # serializer = FruitSerializer(fruit)
            return JsonResponse((serializer.data,), code=201, desc=u'详情页更新成功')
        else:
            return JsonResponse(serializer.errors, code=404, desc=u'数据错误')















