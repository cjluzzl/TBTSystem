#-*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField
from datetime import datetime
from django.utils import timezone
from users.models import UserProfile, Trade
# Create your models here.


class ArticleType(models.Model):
    type_name = models.CharField(max_length=20, verbose_name=u"文章类型", default=u"国内新闻")
    count = models.IntegerField(verbose_name=u"文章数量",default=0)
    add_time = models.DateField(verbose_name=u"添加时间",default=datetime.now)

    class Meta:
        verbose_name = u"文章类型"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.type_name


class Article(models.Model):
    type = models.ForeignKey(ArticleType,verbose_name=u"文章类型")
    new_or_update = models.CharField(verbose_name=u"编辑类型", max_length=6,
                                     choices=(('new', u"新建"), ('update', u"修改")), default="new")
    article_title = models.CharField(max_length=100,verbose_name=u"文章标题",default=u"新文章")
    article_image = models.ImageField(verbose_name=u"封面图", upload_to="images/facephoto", null=True)
    pub_time = models.DateField(default=datetime.now,verbose_name=u"发布日期")
    shortContent = models.CharField(help_text=u"50字以内摘要", verbose_name=u"摘要",max_length=110,null=True,blank=True)
    content = UEditorField(width=900, height=600, imagePath="images/article/ueditor/",
                           filePath="file/article/ueditor/",verbose_name=u"文章内容")
    fav_count = models.IntegerField(default=0, verbose_name=u"点赞数量")
    com_count = models.IntegerField(default=0, verbose_name=u"评论数量")
    url = models.URLField(verbose_name="文章链接", default="http://tbt.cjluzzl.cn/article/1/1.html")
    read_num = models.IntegerField(verbose_name=u"浏览量", default=0)
    trade = models.ForeignKey(Trade,default=1, verbose_name=u"所属行业")
    class Meta:
        verbose_name = u"文章详情"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.article_title

    def save(self, *args, **kwargs):
        if self.new_or_update == "new":
            # 修改文章url
            self.url = "http://miaodu.cjluzzl.cn/article/" + str(self.type.id) + "/" + str(
                Article.objects.count() + 1) + ".html"
            print "当前文章的url:", self.url
            # 对应文章类型下文章数量增加1
            self.type.count = self.type.count + 1
            print "当前的数量 ", self.type.count
            self.type.save()
        else:
            # 修改的时候传给什么值就赋值什么
            pass
        super(self.__class__, self).save(*args, **kwargs)


class ArticleComment(models.Model):
    new_or_update = models.CharField(verbose_name=u"编辑类型", max_length=6,
                                     choices=(('new', u"新建"), ('update', u"修改")), default="new")
    user = models.ForeignKey(UserProfile, verbose_name=u"评论人")
    article = models.ForeignKey(Article, verbose_name=u"所评文章")
    add_time = models.DateTimeField(default=timezone.now, verbose_name=u"评论时间")
    content = models.CharField(max_length=200, verbose_name=u"评论内容")

    class Meta:
        verbose_name = u"文章评论"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user.username + "("+self.user.nick_name+")"

    def save(self, *args, **kwargs):
        if self.new_or_update == "new":
            # 修改文章url
            self.url = "http://miaodu.cjluzzl.cn/article/" + str(self.type.id) + "/" + str(
                Article.objects.count() + 1) + ".html"
            print "当前文章的评论数量:", self.article.com_count
            # 对应文章类型下文章数量增加1
            self.article.com_count = self.article.com_count + 1
            print "当前的数量 ", self.article.com_count
            self.article.save()
        else:
            pass
        super(self.__class__, self).save(*args, **kwargs)