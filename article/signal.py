# -*- coding:utf-8 -*-
__author__ = "cjluzzl"
__date__ = "2017/9/13 0:18 "

import django.dispatch
from django.db.models import signals
from django.dispatch import receiver
from .models import Article
from users.models import PushInfo
from django.core.signals import request_started,request_finished
from utils.send_mail import send_tip_email

pizza_done = django.dispatch.Signal(providing_args=["toppings", "size"])


def callback(sender, **kwargs):
    print("callback")

    print(sender, kwargs)

pizza_done.connect(callback,dispatch_uid="123456")


@receiver(signals.post_save, sender=Article)
def welcome_article(instance, created, **kwargs):
    if created:
        #print send_tip_email("410018832@qq.com","http://127.0.0.1:8000/article/mobile_detail/1")
        print "新增了文章post_save"
        print "instance:", instance
        article = Article.objects.get(article_title=instance)
        print  "article.trade.trad_name",article.trade.trad_name
        #查询PushInfo表
        wait_users = PushInfo.objects.filter(tag=article.trade.trad_name)
        emails = []
        for i in wait_users:
            print i.user.email
            emails.append(i.user.email)

        ##最优方法为使用异步队列发送邮件
        for email in emails:
            state = send_tip_email(email, article.url, send_type="new")
            print "邮箱",email, "发送装态:" , state

        #给表里所有指定tag发邮件


        print "kwargs:",kwargs
    else:
        print "修改了文章post_save"
        print "instance:", instance
        article = Article.objects.get(article_title=instance)
        print  "article.trade.trad_name", article.trade.trad_name
        # 查询PushInfo表
        wait_users = PushInfo.objects.filter(tag=article.trade.trad_name)

        emails = []
        for i in wait_users:
            print i.user.email
            emails.append(i.user.email)

        ##最优方法为使用异步队列发送邮件
        for email in emails:
            state = send_tip_email(email, article.url, send_type="update")
            print "邮箱", email, "发送装态:", state

        # 给表里所有指定tag发邮件


        print "kwargs:", kwargs

#
# @receiver(request_started)
# def create_http(environ, **kwargs):
#     print "建立了http请求"
#     #print environ["HTTP_COOKIE"]
#     print environ["HTTP_USER_AGENT"]
#     print environ["REMOTE_ADDR"]
#
#
# @receiver(request_finished)
# def destory_http(**kwargs):
#     print "http请求结束"
