# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.


class Country(models.Model):
    country_name = models.CharField(max_length=25,verbose_name=u"国家")

    class Meta:
        verbose_name = u"国家信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.country_name


class Province(models.Model):
    province_name = models.CharField(max_length=25,verbose_name=u"省份")

    class Meta:
        verbose_name = u"省份信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.province_name


class Trade(models.Model):
    trad_name = models.CharField(max_length=100,verbose_name=u"行业")

    class Meta:
        verbose_name = u"行业信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.trad_name


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"姓名", default= "")
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(max_length=6, choices=(('male', u"男"), ('female', u"女")), default="female")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="images/head/%Y/%m", default="images/head/default.png", max_length=100)
    country = models.ForeignKey(Country, verbose_name=u"所属国家",null=True)
    province = models.ForeignKey(Province, verbose_name=u"所属省份",null=True)
    trade = models.ForeignKey(Trade, verbose_name=u"所属行业",null=True)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailRevifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    is_alive = models.BooleanField(default=False, verbose_name=u"是否可用")
    send_type = models.CharField(verbose_name=u"验证码类型",choices=(("register", u"注册"), ("forget", u"找回密码")), max_length=10)
    send_time = models.DateField(verbose_name=u"发送时间",default=datetime.now)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email);


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="static/images/banner/%Y/%m", verbose_name=u"轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name


