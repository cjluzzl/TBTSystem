# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-07 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170827_1634'),
        ('article', '0003_article_read_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='shortContent',
            field=models.CharField(blank=True, help_text='50\u5b57\u4ee5\u5185\u6458\u8981', max_length=110, null=True, verbose_name='\u6458\u8981'),
        ),
        migrations.AddField(
            model_name='article',
            name='trade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Trade', verbose_name='\u6240\u5c5e\u884c\u4e1a'),
        ),
    ]
