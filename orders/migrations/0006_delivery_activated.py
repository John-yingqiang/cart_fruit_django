# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-29 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='activated',
            field=models.BooleanField(default=True),
        ),
    ]