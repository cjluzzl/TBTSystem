# -*- coding:utf-8 -*-
__author__ = "cjluzzl"
__date__ = "2017/9/13 0:18 "

import django.dispatch
from django.db.models import signals
from django.dispatch import receiver
from .models import Article
from django.core.signals import request_started,request_finished
pizza_done = django.dispatch.Signal(providing_args=["toppings", "size"])


def callback(sender, **kwargs):
    print("callback")

    print(sender, kwargs)

pizza_done.connect(callback,dispatch_uid="123456")


@receiver(signals.post_save, sender=Article)
def welcome_student(instance, created, **kwargs):
    if created:
        print "新增了文章post_save"
        print instance
        print kwargs
    else:
        print "修改了文章post_save"
        print instance
        print kwargs


@receiver(request_started)
def create_http(environ, **kwargs):
    print "建立了http请求"
    #print environ["HTTP_COOKIE"]
    print environ["HTTP_USER_AGENT"]
    print environ["REMOTE_ADDR"]


@receiver(request_finished)
def destory_http(**kwargs):
    print "http请求结束"
