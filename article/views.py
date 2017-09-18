#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from .models import ArticleType, Article
from users.models import Message
from django.http import HttpResponse
import json
import random
from .signal import pizza_done
from django.shortcuts import render_to_response
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

PERPAGER_ARTICLE_COUNT = 5


class GetMessageView(View):
    def get(self, request, user_name, page_id):
        json_data = {}
        try:
            int(page_id)

        except:
            json_data["retcode"] = "400"
            json_data["meta"] = "非法页面参数"
            return HttpResponse(json.dumps(json_data), content_type="application/json")
        json_data["retcode"] = "200"
        json_data["meta"] = "请求成功"
        l = []
        messages = Message.objects.filter(user_to__username=user_name)[::-1]
        count = len(messages)
        messages = messages[(int(page_id) - 1) * PERPAGER_ARTICLE_COUNT:int(page_id) * PERPAGER_ARTICLE_COUNT]

        for message in messages:
            dic = {}
            dic["send_time"] = str(message.send_time)
            dic["from_user"] = message.user_from.username
            dic["msg"] = message.msg
            l.append(dic)
        json_data["data"] = l
        if (int(page_id)) * PERPAGER_ARTICLE_COUNT < count:
            json_data["more"] = "http://192.168.155.1:8000/users/" + user_name + "/" + str(
                int(page_id) + 1) + "/"
        else:
            json_data["more"] = ""

        return HttpResponse(json.dumps(json_data), content_type="application/json")


def index(request):
    all_articles = Article.objects.all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1


    # Provide Paginator with the request object for complete querystring generation

    p = Paginator(all_articles, 10 , request=request)

    articles = p.page(page)

    return render_to_response('index.html', {
        'all_articles': articles,
    })


class ArticleMobileDetailView(View):
    def get(self, request, article_id):
        article_id = int(article_id)
        article = Article.objects.get(pk=article_id)
        article.read_num += 1
        article.new_or_update = "update"
        article.save()
        return render(request, "article_mobile_detail.html", {"article": article})


class ArticleListView(View):
    def get(self, request, type_id):
        #监听信号
        pizza_done.send(sender='seven', toppings=random.random(), size=random.random())
        type_id = int(type_id)
        print "请求ip" , self.request.META['REMOTE_ADDR']
        articles = Article.objects.filter(type=type_id)
        return render(request, "article_list.html", {"articles": articles})


class ArticleDetailView(View):
    def get(self, request, article_id):
        article_id = int(article_id)
        article = Article.objects.get(pk = article_id)
        article.read_num += 1
        article.new_or_update = "update"
        article.save()
        return render(request, "article_detail.html", {"article": article})


class ArticleJsonView(View):
    def get(self, request, type_id, page_id):
        json_data = {}
        try:
            int(page_id)

        except:
            json_data["retcode"] = "400"
            json_data["meta"] = "非法页面参数"
            return HttpResponse(json.dumps(json_data), content_type="application/json")
        json_data["retcode"] = "200"
        json_data["meta"] = "请求成功"
        l = []
        articles = Article.objects.filter(type=type_id)[::-1]
        count = len(articles)
        articles = articles[(int(page_id) - 1) * PERPAGER_ARTICLE_COUNT:int(page_id) * PERPAGER_ARTICLE_COUNT]

        for article in articles:
            dic = {}
            dic["title"] = article.article_title
            dic["image"] = "http://192.168.155.1:8000/media/" + str(article.article_image)
            dic["type"] = article.type.type_name
            dic["url"] = "http://192.168.155.1:8000/article/mobile_detail/" + str(article.pk) + "/"
            dic["shortContent"] = article.shortContent
            dic["trade"] = article.trade.trad_name
            dic["pubTime"] = str(article.pub_time)
            dic["showCount"] = str(article.read_num)
            l.append(dic)
        json_data["data"] = l
        if (int(page_id)) * PERPAGER_ARTICLE_COUNT < count:
            json_data["more"] = "http://192.168.155.1:8000/article/" + str(int(type_id)) + "/" + str(int(page_id) + 1) + "/"
        else:
            json_data["more"] = ""

        return HttpResponse(json.dumps(json_data), content_type="application/json")


class HomeNewsJsonListView(View):
    def get(self, request, page_id):
        json_data = {}
        try:
            int(page_id)

        except:
            json_data["retcode"] = "400"
            json_data["meta"] = "非法页面参数"
            return HttpResponse(json.dumps(json_data), content_type="application/json")
        json_data["retcode"] = "200"
        json_data["meta"] = "请求成功"
        l = []
        articles = Article.objects.filter(type=1)[::-1]
        count = len(articles)
        articles = articles[(int(page_id) - 1) * PERPAGER_ARTICLE_COUNT:int(page_id) * PERPAGER_ARTICLE_COUNT]

        for article in articles:
            dic = {}
            dic["title"] = article.article_title
            dic["image"] = "http://192.168.155.1:8000/media/" + str(article.article_image)
            dic["type"] = article.type.type_name
            dic["url"] = "http://192.168.155.1:8000/article/mobile_detail/" + str(article.pk) + "/"
            dic["shortContent"] = article.shortContent
            dic["trade"] = article.trade.trad_name
            dic["pubTime"] = str(article.pub_time)
            dic["showCount"] = str(article.read_num)
            l.append(dic)
        json_data["data"] = l
        if (int(page_id)) * PERPAGER_ARTICLE_COUNT < count:
            json_data["more"] = "http://192.168.155.1:8000/article/home_news_list/" + str(int(page_id) + 1) + "/"
        else:
            json_data["more"] = ""

        return HttpResponse(json.dumps(json_data), content_type="application/json")


class AbroadNewsJsonListView(View):
    def get(self, request, page_id):
        json_data = {}
        try:
            int(page_id)

        except:
            json_data["retcode"] = "400"
            json_data["meta"] = "非法页面参数"
            return HttpResponse(json.dumps(json_data), content_type="application/json")
        json_data["retcode"] = "200"
        json_data["meta"] = "请求成功"
        l = []
        articles = Article.objects.filter(type=2)[::-1]
        count = len(articles)
        articles = articles[(int(page_id) - 1) * PERPAGER_ARTICLE_COUNT:int(page_id) * PERPAGER_ARTICLE_COUNT]

        for article in articles:
            dic = {}
            dic["title"] = article.article_title
            dic["image"] = "http://192.168.155.1:8000/media/" + str(article.article_image)
            dic["type"] = article.type.type_name
            dic["url"] = "http://192.168.155.1:8000/article/mobile_detail/" + str(article.pk) + "/"
            dic["trade"] = article.trade.trad_name
            dic["pubTime"] = str(article.pub_time)
            dic["showCount"] = str(article.read_num)
            dic["shortContent"] = article.shortContent
            l.append(dic)
        json_data["data"] = l
        if (int(page_id)) * PERPAGER_ARTICLE_COUNT < count:
            json_data["more"] = "http://192.168.155.1:8000/article/abroad_news_list/" + str(int(page_id) + 1) + "/"
        else:
            json_data["more"] = ""

        return HttpResponse(json.dumps(json_data), content_type="application/json")
