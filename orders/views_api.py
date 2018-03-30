# coding=utf-8
from rest_framework.views import APIView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from common.return_format import JsonResponse
from .models import OrderItem, Order, Delivery
from .serializer import OrderSerializer, OrderItemSerializer, DeliverySerializer
from .forms import OrderCreateForm
from cart.cart import Cart

class OrderList(APIView):
    def get(self, request, paid=False):
        orders = Order.objects.filter(paid=paid)
        if orders:
            serializer = OrderSerializer(orders, many=True)
            return JsonResponse(data=serializer.data, code=200, desc=u'订单列表')
        else:
            return JsonResponse(data='', code=200, desc=u'订单列表为空')

    def post(self, request):
        cart = Cart(request)
        form = OrderSerializer(request.data)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                        order = order,
                        product = item['product'],
                        price = item['price'],
                        quantity = item['quantity'])
            cart.clear()
            return HttpResponseRedirect(reverse('orders:order_list'))

class OrderDetail(APIView):
    def get_order(self, pk):
        try:
            return Order.objects.get(id=int(pk))
        except Order.DoesNotExist:
            return None

    def get(self, request, pk):
        order = self.get_order(pk)

        if order:
            serializer = OrderSerializer(order)
            return JsonResponse(data=serializer.data, code=200, desc=u'订单详情')
        else:
            return JsonResponse(data='', code=404, desc=u'订单为空')

    def put(self, request, pk):
        order = self.get_order(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, code=404, desc=u'数据验证错误')

                        
        
