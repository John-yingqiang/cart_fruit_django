# fruit/apps.py
from __future__ import unicode_literals

from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class FruitConfig(AppConfig):
    name = 'fruit'

class SuitConfig(DjangoSuitConfig):
	layout = 'horizontal'