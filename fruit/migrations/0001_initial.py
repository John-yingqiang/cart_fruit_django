# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 05:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_thumbs.db.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, verbose_name='\u6d3b\u52a8\u7c7b\u578b')),
                ('image', django_thumbs.db.models.ImageWithThumbsField(null=True, upload_to='static/images/activity')),
            ],
            options={
                'verbose_name': '\u9996\u9875\u6700\u65b0\u6d3b\u52a8\u56fe\u7247,\u4e3a\u4e86\u7f8e\u89c2\uff0c\u56fe\u7247\u5927\u5c0f\u4e0d\u8981\u76f8\u5dee\u592a\u591a',
                'verbose_name_plural': '\u9996\u9875\u6700\u65b0\u6d3b\u52a8\u56fe\u7247,\u4e3a\u4e86\u7f8e\u89c2\uff0c\u56fe\u7247\u5927\u5c0f\u4e0d\u8981\u76f8\u5dee\u592a\u591a',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '\u5404\u4e2a\u7c7b\u578b\u56fe\u7247\u5927\u5c0f\u8bf4\u660e([\u6c34\u679c:Image icon(420x230) Image content(1920x1100)] [\u9996\u9875\u6700\u65b0\u6d3b\u52a8\u56fe\u7247:(1440x775)])',
                'verbose_name_plural': '\u5404\u4e2a\u7c7b\u578b\u56fe\u7247\u5927\u5c0f\u8bf4\u660e([\u6c34\u679c:Image icon(420x230) Image content(1920x1100)] [\u9996\u9875\u6700\u65b0\u6d3b\u52a8\u56fe\u7247:(1440x775)])',
            },
        ),
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u6807\u9898')),
                ('image_icon', django_thumbs.db.models.ImageWithThumbsField(upload_to='static/images/app')),
                ('image_content1', django_thumbs.db.models.ImageWithThumbsField(blank=True, upload_to='static/images/app')),
                ('image_content2', django_thumbs.db.models.ImageWithThumbsField(blank=True, upload_to='static/images/app')),
                ('image_content3', django_thumbs.db.models.ImageWithThumbsField(blank=True, upload_to='static/images/app')),
                ('datetime', models.DateTimeField(auto_now=True, verbose_name='\u6dfb\u52a0\u65e5\u671f')),
                ('content', models.TextField(verbose_name='\u7b80\u4ecb(\u5bf9\u6807\u9898\u7684\u7b80\u8ff0)')),
                ('detail', models.TextField(blank=True, verbose_name='\u4ea7\u54c1\u8be6\u60c5')),
                ('kinds', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='\u6c34\u679c\u5206\u7c7b')),
                ('slug', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fruits_in_activity', to='fruit.Activity', verbose_name='\u53c2\u52a0\u7684\u6d3b\u52a8\u7c7b\u578b')),
            ],
            options={
                'verbose_name': '\u6c34\u679c',
                'verbose_name_plural': '\u6c34\u679c',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u89c6\u9891\u6807\u9898')),
                ('video', models.FileField(null=True, upload_to='static/media', verbose_name='\u8def\u5f84')),
                ('content', models.TextField(blank=True, verbose_name='\u7b80\u4ecb(\u5efa\u8bae\u4e3a\u7a7a)')),
            ],
            options={
                'verbose_name': '\u679c\u56ed\u89c6\u9891',
                'verbose_name_plural': '\u679c\u56ed\u89c6\u9891',
            },
        ),
    ]
