# coding=utf-8
from models import Fruit
from taggit.models import Tag

def filter_kinds(filter_by):
    result = Fruit.objects.filter(**filter_by)


