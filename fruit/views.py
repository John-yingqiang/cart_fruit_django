# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Fruit, Activity, Video
from random import randrange
from taggit.admin import Tag
from django.utils.encoding import smart_str, smart_unicode
from django.http import HttpResponse
from cart.forms import CartAddProductForm
# Create your views here.
def index(request):
	banners = Activity.objects.all()
	kinds = Tag.objects.all()
	all_fruit = {}
	form = CartAddProductForm()
	
	for kind in kinds:
		fruit = Fruit.objects.filter(kinds__in=[kind])[:6]
		all_fruit[smart_unicode(kind)] = fruit

	if request.method == "POST":
		fruits = Fruit.objects.filter(title__contains=request.POST['query'])
		return render(request, 'search.html', {'fruits': fruits})

	return render(request, "index.html", {"banners": banners,
										  "all_fruit": all_fruit,
										  "form": form})

def aboutus(self):
	return render_to_response("aboutus.html")

def contact(self):
	return render_to_response("contact.html")

def more(request, tags):
	if request.method == "POST":
		fruits = Fruit.objects.filter(title__contains=request.POST['query'])
		return render(request, 'search.html', {'fruits': fruits})
	tag = get_object_or_404(Tag, name=smart_unicode(tags))
	all_fruit = Fruit.objects.filter(kinds__in=[tag])
	return render(request, "more.html", {"kind": tags,
										 "fruits": all_fruit})

def relative_activity(request, id):
	act = get_object_or_404(Activity, id=id)
	if act:
		fruits = act.fruits_in_activity.all()
		return render(request, 'discount.html', {'fruits':fruits,
												 'activity': act})

def detail(request, id):
	id = int(id)
	single = Fruit.objects.get(id=id)
	single_next1 = single_next2 = single_pre = single

	if id > 1:
		single_pre = Fruit.objects.get(id=id-1)
		try:
			single_next1 = Fruit.objects.get(id=id+1)
			single_next2 = Fruit.objects.get(id=id+2)
		except Exception:
			pass
	else:
		try:
			single_pre = Fruit.objects.get(id=id+1)
			single_next1 = Fruit.objects.get(id=id+2)
			single_next2 = Fruit.objects.get(id=id+3)
		except Exception:
			pass

	return render(request, "generic.html", {"single": single, 
										   "single_pre": single_pre, 
										   "single_next1": single_next1, 
										   "single_next2": single_next2})

def get_video(request):
	if request.method == "POST":
		videos = Video.objects.filter(title__contains=request.POST['query'])
		return render(request, 'search_video.html', {'videos': videos})
	videos = Video.objects.all()
	return render(request, 'video.html', {'videos': videos})