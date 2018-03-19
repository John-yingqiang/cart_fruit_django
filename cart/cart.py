 # -*- coding: UTF-8 -*- 
from decimal import Decimal
from django.conf import settings
from fruit.models import Fruit

class Cart(object):
	def __init__(self, request):
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart

	def add(self, product, quantity=1, update_quantity=False):
		product_id = str(product.id)
		if product_id not in self.cart:
			self.cart[product_id] = {'quantity': 0, 'price':str(product.price)}

		if update_quantity:
			self.cart[product_id]['quantity'] = quantity
		else:
			self.cart[product_id]['quantity'] += quantity
		self.save()

	def save(self):
		self.session[settings.CART_SESSION_ID] = self.cart
		# update the session cart
		self.session.modified = True
		#mark the session as 'modified' to make sure it is saved

	def remove(self, product):
		product_id = str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()

	def __iter__(self):
		# 我们将迭代购物车当中的物品，然后获取相应的 Product 实例
		product_ids = self.cart.keys()
		products = Fruit.objects.filter(id__in=product_ids)
		
		for product in products:
			self.cart[str(product.id)]['product'] = product

		for item in self.cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['quantity']
			yield item

	def __len__(self):
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):
		return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

	def clear(self):
		del self.session[settings.CART_SESSION_ID]
		self.session.modified = True















