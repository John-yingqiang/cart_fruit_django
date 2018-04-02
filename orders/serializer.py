from rest_framework import serializers
from models import Order, Delivery, OrderItem
from fruit.serializer import FruitSerializer
from .status import Status

class OrderSerializer(serializers.ModelSerializer):
    delivery = serializers.StringRelatedField(many=True)
    order_items = serializers.StringRelatedField(many=True)

    class Meta:
        model = Order
        fields = '__all__'

class OrderPutSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, required=False)
    email = serializers.EmailField(required=False)
    address = serializers.CharField(max_length=250, required=False)
    postal_code = serializers.CharField(max_length=20, required=False)
    city = serializers.CharField(max_length=100, required=False)
    order_num = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

    class Meta:
        model = Order
        fields = '__all__'
    
    def validate_status(self, value):
        status = Status.status_sort.keys()
        
        if value in status:
            return value
        else:
            raise serializers.ValidationError('{} must in {}'.format(value, status))


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

