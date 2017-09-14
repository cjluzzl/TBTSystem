# -*- coding:utf-8 -*-
__author__ = "cjluzzl"
__date__ = "2017/8/26 16:09 "
import xadmin
from xadmin import views
from .models import Province,Country,Trade


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


xadmin.site.register(Country, CountryAdmin)
xadmin.site.register(Province, ProvinceAdmin)
xadmin.site.register(Trade, TradeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)#主题注册
xadmin.site.register(views.CommAdminView, GlobalSetting)#更改网站标题和公司名注册