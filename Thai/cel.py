# -*- coding: utf-8 -*-
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Thai.settings')

app = Celery('Thai')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
'''
我们为 Celery 命令行程序设置了 DJANGO_SETTINGS_MODULE 变量。
然后我们用  app=Celery('myshop') 创建了一个实例。我们用 config_from_object() 方法来加载项目设置中任意的定制化配置。
最后，我们告诉 Celery 自动查找我们列举在 INSTALLED_APPS 设置中的异步应用任务。
Celery 将在每个应用路径下查找 task.py 来加载定义在其中的异步任务。
'''