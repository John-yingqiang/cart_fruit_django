# coding=utf-8
from rest_framework.views import APIView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from common.return_format import JsonResponse
from .models import OrderItem, Order, Delivery
from .serializer import OrderSerializer, OrderItemSerializer, DeliverySerializer, OrderPutSerializer
from .forms import OrderCreateForm
from cart.cart import Cart
from .status import Status

class OrderList(APIView):
    def get(self, request):
        orders = Order.objects.all()
        if orders:
            serializer = OrderSerializer(orders, many=True)
            return JsonResponse(data=serializer.data, code=200, desc=u'订单列表')
        else:
            return JsonResponse(data='', code=200, desc=u'订单列表为空')

    def post(self, request):
        cart = Cart(request)
        request.data['price']=cart.get_total_price()
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
    
    def put(self, request, id):
        def change_order_status(order, status):
            if Status.check_status(status, order.status):
                order.status = status
                order.save()
                return HttpResponseRedirect(reverse('orders:order_detail',kwargs={'pk':id}))
            return JsonResponse(data='', code=404, desc='订单状态无法跨级更改')

        
        if not request.data:
            return JsonResponse(data='', code=400, desc=u'无数据，订单没有修改')
        try:
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return JsonResponse(data='', code=404, desc='订单不存在')
        
        serializer = OrderPutSerializer(data=request.data)
        if serializer.is_valid():
            if request.data.get('status', None):
                return change_order_status(order, request.data.get('data'))
            
        else:
            return JsonResponse(data=serializer.errors, code=404, desc='数据错误')


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
        if not request.data:
            return JsonResponse('', code=404, desc=u'数据为空')
        serializer = OrderPutSerializer(order, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, code=200, desc='订单修改后详情')
        return JsonResponse(serializer.errors, code=404, desc=u'数据验证错误')

                        
        
