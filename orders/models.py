# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from fruit.models import Fruit
# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'姓名')
    email = models.EmailField(verbose_name=u'邮件')
    address = models.CharField(max_length=250, verbose_name=u'地址')
    postal_code = models.CharField(max_length=20, verbose_name=u'邮编')
    city = models.CharField(max_length=100, verbose_name=u'城市') 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    order_num = models.CharField(max_length=20, verbose_name=u'订单编号')
    status = models.CharField(default='created', max_length=10, verbose_name=u'订单状态')
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name=u'总价')
    drawback = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name=u'退款')

    class Meta:
    	ordering = ('-created',)

    def __str__(self):
    	return 'Order {}'.format(self.id)

    def get_total_cost(self):
    	return sum(item.get_cost() for item in self.items.all())

class Delivery(models.Model):
    '''物流信息'''
    order = models.ForeignKey(Order, related_name='delivery')
    position = models.CharField(max_length=50, verbose_name=u'收件人地址')
    as_p_name = models.CharField(max_length=20, verbose_name=u'收件人名字')
    as_p_phone = models.CharField(max_length=15, verbose_name=u'收件人电话')
    delivery_num = models.CharField(max_length=20, verbose_name=u'运单编号')
    activated = models.BooleanField(default=True)

    def __str__(self):
        return 'name:{}, phone:{}, delivery_num:{}'.format(self.as_p_name, self.as_p_phone, self.delivery_num)

class Payment(models.Model):
    pass


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items')
    product = models.ForeignKey(Fruit, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    delivery = models.ForeignKey(Delivery, related_name='order_items', blank=True, null=True)

    def __str__(self):
        return 'fruit:{}, price:{}, quantity:{}'.format(self.product.id, self.price, self.quantity)

    def get_cost(self):
    	return self.price * self.quantity
