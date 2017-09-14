# -*- coding:utf-8 -*-
__author__ = "cjluzzl"
__date__ = "2017/8/27 17:29 "

import xadmin
from .models import Tbt, Sps


class TbtAdmin(object):
    list_display = ['tbt_title','tbt_num', 'ics_num', 'tbt_member','aim','short_content','pub_time','end_time']
    search_display = ['tbt_title','tbt_num', 'ics_num', 'tbt_member','aim','short_content','content']
    list_filter = ['tbt_title','tbt_num', 'ics_num', 'tbt_member','aim','pub_time','end_time','short_content','content']
    style_fields = {"content": "ueditor"}


class SpsAdmin(object):
    list_display = ['sps_title', 'sps_num', 'ics_num', 'tbt_member', 'aim', 'short_content', 'pub_time', 'end_time']
    search_display = ['sps_title', 'sps_num', 'ics_num', 'tbt_member', 'aim', 'short_content', 'content']
    list_filter = ['sps_title', 'sps_num', 'ics_num', 'tbt_member', 'aim', 'pub_time', 'end_time', 'short_content', 'content']
    style_fields = {"content": "ueditor"}


xadmin.site.register(Tbt, TbtAdmin)
xadmin.site.register(Sps, SpsAdmin)