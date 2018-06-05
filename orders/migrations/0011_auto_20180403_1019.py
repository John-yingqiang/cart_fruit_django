# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-03 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_order_drawback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='drawback',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='\u9000\u6b3e'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='\u603b\u4ef7'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='created', max_length=10, verbose_name='\u8ba2\u5355\u72b6\u6001'),
        ),
    ]
