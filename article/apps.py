#-*- coding:utf-8 -*-

from django.apps import AppConfig


class ArticleConfig(AppConfig):
    name = 'article'
    verbose_name = u"文章管理"

    def ready(self):
        print "文章管理启动了"
