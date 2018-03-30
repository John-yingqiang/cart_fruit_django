# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django_thumbs.db.models import ImageWithThumbsField
from django.db import models
from django.core.urlresolvers import reverse
import os
from taggit.managers import TaggableManager
import sys;
reload(sys);
sys.setdefaultencoding("utf8")


# Create your models here.
class Video(models.Model):
	title = models.CharField(max_length=100, verbose_name=u"视频标题")
	video = models.FileField(upload_to='static/media', null=True, verbose_name=u"路径")
	content = models.TextField(blank=True, verbose_name=u"简介(建议为空)")

	def filename(self):
		return os.path.basename(self.title)

	def __unicode__(self):
		return u"{}".format(self.title)

	class Meta:
		verbose_name = u"果园视频"
		verbose_name_plural = u"果园视频"

class Activity(models.Model):
	category = models.CharField(max_length=100, verbose_name=u"活动类型")
	image = ImageWithThumbsField(upload_to="static/images/activity", null=True)

	def __unicode__(self):
		return u"{}, id:{}".format(self.category, self.id)

	class Meta:
		verbose_name = u"首页最新活动图片,为了美观，图片大小不要相差太多"
		verbose_name_plural = u"首页最新活动图片,为了美观，图片大小不要相差太多"

        @property
        def full_image(self):
            return "http://118.31.43.180" + self.image.url

class Fruit(models.Model):
	title = models.CharField(max_length=255, verbose_name=u"标题")
	kinds = TaggableManager(verbose_name=u"水果分类")
	slug = models.ForeignKey(Activity, null=True, blank=True, related_name="fruits_in_activity", verbose_name=u"参加的活动类型")
	image_icon = ImageWithThumbsField(u"首页图片(273x150)", upload_to="static/images/app", sizes=((273,150),))
	image_content1 = ImageWithThumbsField(upload_to="static/images/app", blank=True, help_text=u"详细图片(可空)")
	image_content2 = ImageWithThumbsField(upload_to="static/images/app", blank=True, verbose_name=u"详细图片(可空)")
	image_content3 = ImageWithThumbsField(upload_to="static/images/app", blank=True, verbose_name=u"详细图片(可空)")
	datetime = models.DateTimeField(auto_now=True, verbose_name=u"添加日期")
	content = models.TextField(verbose_name=u"简介(对标题的简述)")
	detail = models.TextField(verbose_name=u"产品详情", blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=10)
        count = models.IntegerField(default=100, verbose_name=u'库存')

	def __unicode__(self):
 		return u"{}".format(self.title)

	class Meta:
            ordering = ['title']
            verbose_name = u"水果"
            verbose_name_plural = u"水果"
        
        @property
        def full_image_content1(self):
            if hasattr(self.image_content1, 'url'):
                return "http://118.31.43.180" + self.image_content1.url
            return ""

        @property
        def full_image_icon(self):
            return "http://118.31.43.180" + self.image_icon.url

        @property
        def tag_name(self):
            try:
                return self.kinds.values()[0]["name"]
            except Exception:
                return ""


class Document(models.Model):
	class Meta:
		verbose_name = u"各个类型图片大小说明([水果:Image icon(420x230) Image content(1920x1100)] [首页最新活动图片:(1440x775)])"
		verbose_name_plural = u"各个类型图片大小说明([水果:Image icon(420x230) Image content(1920x1100)] [首页最新活动图片:(1440x775)])"
		
