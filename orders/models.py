# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from fruit.models import Fruit
# Create your models here.
class Order(models.Model):
	name = models.CharField(max_length=50, verbose_name='姓名')
	email = models.EmailField(verbose_name='邮件')
	address = models.CharField(max_length=250, verbose_name='地址')
	postal_code = models.CharField(max_length=20, verbose_name='邮编')
	city = models.CharField(max_length=100, verbose_name='城市') 
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False, verbose_name='已完成支付')# 使用这个字段来区分支付和未支付订单

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return 'Order {}'.format(self.id)

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items')
	product = models.ForeignKey(Fruit, related_name='order_items')
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return '{}'.format(self.id)

	def get_cost(self):
		return self.price * self.quantity