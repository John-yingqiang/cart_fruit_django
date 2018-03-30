# coding=utf-8
from rest_framework.decorators import api_view
from django.http import HttpResponseRedirect
from common.return_format import JsonResponse
from django.shortcuts import get_object_or_404
from .cart import Cart
from .forms import CartAddProductForm
from fruit.models import Fruit
from django.core.urlresolvers import reverse

@api_view(['POST'])
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Fruit, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                quantity=cd['quantity'],
                update_quantity=cd['update'])
        return HttpResponseRedirect(reverse('cart:cart_detail'))
    else:
        return JsonResponse(data=[form.errors.as_json()], code=404, desc=u'数据错误')

@api_view(['GET'])
def cart_detail(request):
    cart = Cart(request) 

    return JsonResponse(data=cart.serializer(), code=200, desc=u'购物车详情')

@api_view(['GET'])
def cart_clear(request):
    Cart(request).clear()

    return HttpResponseRedirect(reverse('cart:cart_detail'))
    
