# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-02 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='drawback',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
