# -*- coding:utf-8 -*-
__author__ = "cjluzzl"
__date__ = "2017/8/28 18:32 "

from django.conf.urls import url, include
from django.views.generic import TemplateView
from .views import TBTView, SPSView, TBTListView, SPSListView

urlpatterns = [
    url(r'tbt_list/(?P<page_num>.*)/$',TBTListView.as_view(), name="tbt_list"),
    url(r'sps_list/(?P<page_num>.*)/$',SPSListView.as_view(), name="sps_list"),
    url(r'tbt/(?P<tbt_num>.*)/$', TBTView.as_view(), name="tbtsps_tbt"),
    url(r'sps/(?P<sps_num>.*)/$', SPSView.as_view(), name="tbtsps_sps")
]