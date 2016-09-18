# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=10000, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(blank=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]
