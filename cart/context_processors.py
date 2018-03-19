# -*- coding: utf-8 -*-
from .cart import Cart

def cart(request):
	return {'cart': Cart(request)}
	# 一个上下文处理器是一个函数，这个函数接收一个 request 对象作为参数，然后返回一个对象字典
	# 上下文处理器会在所有的使用 RequestContext 的请求中执行。你可能想要创建一个定制的模板标签来代替一个上下文处理器，如果你想要链接到数据库的话