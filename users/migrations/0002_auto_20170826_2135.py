# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-26 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Country', verbose_name='\u6240\u5c5e\u56fd\u5bb6'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Province', verbose_name='\u6240\u5c5e\u7701\u4efd'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='trade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Trade', verbose_name='\u6240\u5c5e\u884c\u4e1a'),
        ),
    ]
