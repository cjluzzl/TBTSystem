# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-28 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tbtsps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sps',
            name='sps_title',
            field=models.CharField(default='\u8bf7\u8f93\u5165\u6807\u9898', max_length=200, verbose_name='\u901a\u62a5\u6807\u9898'),
        ),
        migrations.AddField(
            model_name='tbt',
            name='tbt_title',
            field=models.CharField(default='\u8bf7\u8f93\u5165\u6807\u9898', max_length=200, verbose_name='\u901a\u62a5\u6807\u9898'),
        ),
    ]