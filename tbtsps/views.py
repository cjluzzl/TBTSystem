#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from .models import Tbt, Sps
# Create your views here.

PER_PAGE_NUM = 10


class TBTListView(View):
    def get(self, request, page_num):
        page_num = int(page_num)
        all_tbt = Tbt.objects.all()
        all_num = len(all_tbt)
        tbt_lists = all_tbt.reverse()[(page_num-1)*10:page_num*10]
        return render(request, "tbt_index.html",{"all_num": all_num, "tbt_lists":tbt_lists})


class SPSListView(View):
    def get(self, request, page_num):
        page_num = int(page_num)
        all_sps = Sps.objects.all()
        all_num = len(all_sps)
        sps_lists = all_sps.reverse()[(page_num-1)*10:page_num*10]
        return render(request, "sps_index.html",{"all_num": all_num, "sps_lists": sps_lists})

class TBTView(View):
    def get(self, request, tbt_num):
        tbt_num = int(tbt_num)
        tbt = Tbt.objects.get(pk=tbt_num)
        tbt.read_num = tbt.read_num + 1
        tbt.save()
        return render(request, "tbt.html",{"tbt":tbt})


class SPSView(View):
    def get(self, request, sps_num):
        sps_num = int(sps_num)
        sps = Sps.objects.get(pk=sps_num)
        sps.read_num += 1
        sps.save()
        return render(request, "sps.html", {"sps": sps})

