#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField
from datetime import datetime
from django.utils import timezone
from users.models import Trade
# Create your models here.


class Tbt(models.Model):
    tbt_trad = models.ForeignKey(Trade, default=1, verbose_name=u"所属行业")
    tbt_title = models.CharField(max_length=200,verbose_name=u"通报标题", default=u"请输入标题")
    tbt_num = models.CharField(max_length=100, verbose_name=u"通报号")
    ics_num = models.CharField(max_length=100, verbose_name=u"ICS号")
    pub_time = models.DateField(verbose_name=u"发布日期", default=datetime.now)
    end_time = models.DateField(verbose_name=u"截止日期", default=datetime.now)
    tbt_member = models.CharField(max_length=100,verbose_name=u"通报成员",default=u"请输入成员名")
    aim = models.CharField(max_length=100, verbose_name=u"目标和理由", default=u"保护环境")
    short_content = models.CharField(max_length=300, verbose_name=u"内容概述")
    content = UEditorField(width=900, height=600, imagePath="images/tbt/ueditor/",
                           filePath="file/tbt/ueditor/",verbose_name=u"正文")
    read_num = models.IntegerField(verbose_name=u"浏览量", default=0)
    class Meta:
        verbose_name = u"WTO/TBT通报"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "{0}(1)".format(self.tbt_member, self.tbt_num)


class Sps(models.Model):
    sps_trad = models.ForeignKey(Trade, default=1, verbose_name=u"所属行业")
    sps_title = models.CharField(max_length=200, verbose_name=u"通报标题", default=u"请输入标题")
    sps_num = models.CharField(max_length=100, verbose_name=u"通报号")
    ics_num = models.CharField(max_length=100, verbose_name=u"ICS号")
    pub_time = models.DateField(verbose_name=u"发布日期", default=datetime.now)
    end_time = models.DateField(verbose_name=u"截止日期", default=datetime.now)
    tbt_member = models.CharField(max_length=100,verbose_name=u"通报成员",default=u"请输入成员名")
    aim = models.CharField(max_length=100, verbose_name=u"目标和理由", default=u"保护环境")
    short_content = models.CharField(max_length=200, verbose_name=u"内容概述")
    content = UEditorField(width=900, height=600, imagePath="images/sps/ueditor/",
                           filePath="file/sps/ueditor/",verbose_name=u"正文")
    read_num = models.IntegerField(verbose_name=u"浏览量", default=0)

    class Meta:
        verbose_name = u"WTO/SPS通报"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "{0}(1)".format(self.tbt_member, self.sps_num)
