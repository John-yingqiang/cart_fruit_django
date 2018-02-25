# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruit',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10),
        ),
    ]
