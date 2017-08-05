# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_author_blog_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='headline',
            field=models.CharField(max_length=200, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发表时间'),
        ),
        migrations.AlterField(
            model_name='reporter',
            name='full_name',
            field=models.CharField(max_length=70, verbose_name='作者'),
        ),
    ]