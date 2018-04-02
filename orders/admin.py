# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
class OrderItemInline(admin.TabularInline):
	model = OrderItem
	raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'email',
					'address', 'postal_code', 'city',
					'created', 'updated']
	list_filter = ['created', 'updated']
	inlines = [OrderItemInline]

	def __unicode__(self):
		return u'订单'

admin.site.register(Order, OrderAdmin)
# 我们在  OrderItem 使用 ModelInline 来把它引用为  OrderAdmin 类的
# 内联元素。一个内联元素允许你在同一编辑页引用模型，并且将这个模型作为父模型
