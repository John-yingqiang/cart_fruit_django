from rest_framework import serializers
from models import Order, Delivery, OrderItem
from fruit.serializer import FruitSerializer


class OrderSerializer(serializers.ModelSerializer):
    delivery = serializers.StringRelatedField(many=True)
    order_items = serializers.StringRelatedField(many=True)

    class Meta:
        model = Order
        fields = '__all__'

class OrderPutSerializer(serializer.ModelSerializer):


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    product = FruitSerializer()
    
    class Meta:
        model = OrderItem
        fields = '__all__'

class DeliverySerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    
    class Meta:
        model = Delivery
        fields = '__all__'

