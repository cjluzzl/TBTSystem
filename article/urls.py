# -*- coding:utf-8 -*-
__author__ = "cjluzzl"
__date__ = "2017/8/29 15:02 "

from django.conf.urls import url, include
from django.views.generic import TemplateView
from .views import ArticleListView, ArticleDetailView, HomeNewsJsonListView, AbroadNewsJsonListView, ArticleJsonView


urlpatterns = [
    url(r'^article_type/(?P<type_id>.*)/$', ArticleListView.as_view(), name="article_list"),
    url(r'^get_article_json/(?P<type_id>.*)/(?P<page_id>.*)/$',ArticleJsonView.as_view(), name="article_json"),
    url(r'^detail/(?P<article_id>.*)/$', ArticleDetailView.as_view(), name="article_detail"),
    url(r'^home_news_list/(?P<page_id>.*)/$', HomeNewsJsonListView.as_view(), name="home_news_list"),
    url(r'^abroad_news_list/(?P<page_id>.*)/$', AbroadNewsJsonListView.as_view(), name="abroad_news_list"),
]