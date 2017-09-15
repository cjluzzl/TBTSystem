# -*- coding:utf-8 -*-
__author__ = "cjluzzl"
__date__ = "2017/8/29 13:41 "

from django.conf.urls import url, include
from django.views.generic import TemplateView
from .views import LoginView, LogoutView, RegisterView, ForgetPwdView, ActiveUserView, test


urlpatterns = [
    url(r'active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    url(r'login/$', LoginView.as_view(), name="user_login"),
    url(r'logout/$', LogoutView.as_view(), name="user_logout"),
    url(r'test/(?P<user_name>.*)/$', test)
]