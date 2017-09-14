# -*- coding:utf-8 -*-
__author__ = "cjluzzl"
__date__ = "2017/8/27 16:10 "

import xadmin
from .models import ArticleType, Article, ArticleComment


class ArticleTypeAdmin(object):
    list_display = ['type_name', 'count', 'add_time']
    search_display = ['type_name', 'count']
    list_filter = ['type_name', 'count', 'add_time']


class ArticleAdmin(object):
    list_display = ['type', 'article_title', 'pub_time']
    search_display = ['type__type_name', 'article_title','content']
    list_filter = ['type', 'article_title', 'pub_time', 'content']
    style_fields = {"content": "ueditor"}


class ArticleCommentAdmin(object):
    list_display = ['user', 'article', 'add_time']
    search_display = ['user__nick_name', 'article__article_title']
    list_filter = ['user', 'article', 'add_time', 'content']


xadmin.site.register(ArticleType, ArticleTypeAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(ArticleComment, ArticleCommentAdmin)