from rest_framework.decorators import api_view
from serializer import FruitSerializer
from rest_framework.response import Response
from models import Fruit

@api_view(['GET', 'POST'])
def fruit_list(request):
    if request.method == 'GET':
        fruits = Fruit.objects.all()
        serializer = FruitSerializer(fruits, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        fruit = FruitSerializer(data=request.data)
        if fruit.is_valid():
            fruit.save()
        else:
            Response(fruit.errors)

@api_view(['GET'])
def get_absolute_url(request, url):
    return 

@api_view(['GET'])
def fruit_detail(request, id):
    try:
        fruit = Fruit.objects.get(pk=int(id))
    except Fruit.DoesNotExist:
        return Response({"error":"name"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FruitSerializer(fruit)
        return Response(serializer.data)
        

