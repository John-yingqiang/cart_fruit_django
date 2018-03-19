# -*- coding: utf-8 -*-
from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
	'''
		send email when an order is successfully created
	'''
	order = Order.objects.get(id=order_id)
	subject = '已成功下单，订单号:{}'.format(order_id)
	message = '尊敬的{}，\n你的订单已经成功提交，订单号是:{}'.format(order.name, order.id)

	mail_sent = send_mail(subject, message, '850069854@qq.com', [order.email])

	return mail_send

'''
一个 Celery 任务 只是一个用 task 装饰的 Python 函数
'''