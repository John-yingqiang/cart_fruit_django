# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-30 11:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20180330_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='paid',
        ),
    ]