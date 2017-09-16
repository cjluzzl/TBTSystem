# -*- coding:utf-8 -*-
__author__ = "cjluzzl"
__date__ = "2017/8/26 16:09 "
import xadmin
from xadmin import views
from .models import Province, Country, Trade, Message


#主题注册
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


#更改网站标题和公司名注册
class GlobalSetting(object):
    site_title = u"TBT后台管理系统"
    site_footer = u"power by cjluzzl"
    menu_style = "accordion"


class CountryAdmin(object):
    list_display = ['country_name']
    search_fields = ['country_name']
    list_filter = ['country_name']


class ProvinceAdmin(object):
    list_display = ['province_name']
    search_display = ['province_name']
    list_filter = ['province_name']


class TradeAdmin(object):
    list_display = ['trad_name']
    search_display = ['trad_name']
    list_filter = ['trad_name']


class MessageAdmin(object):
    """from_user = models.ForeignKey(UserProfile, verbose_name=u"发送人")
    to_user = models.ForeignKey(UserProfile, verbose_name=u"接收人")
    read_state = models.BooleanField(default=False, verbose_name="读取状态")
    del_state = models.BooleanField(default=False, verbose_name=u"是否被删除")
    send_time = models.DateTimeField(default=timezone.now, verbose_name=u"发送时间")
    msg = models.CharField(max_length=1000, verbose_name=u"消息内容", help_text=u"不超过500字")"""
    list_display = ['user_from', 'user_to', 'read_state', 'del_state', 'msg', 'send_time']
    search_display = ['user_from', 'user_to', 'read_state', 'del_state', 'msg']
    list_filter = ['user_from', 'user_to', 'read_state', 'del_state', 'msg', 'send_time']

xadmin.site.register(Country, CountryAdmin)
xadmin.site.register(Province, ProvinceAdmin)
xadmin.site.register(Trade, TradeAdmin)
xadmin.site.register(Message, MessageAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)#主题注册
xadmin.site.register(views.CommAdminView, GlobalSetting)#更改网站标题和公司名注册