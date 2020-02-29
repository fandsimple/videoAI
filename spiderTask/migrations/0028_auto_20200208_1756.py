# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2020-02-08 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiderTask', '0027_recret_songname'),
    ]

    operations = [
        migrations.AddField(
            model_name='recret',
            name='source',
            field=models.CharField(default='热歌推介', max_length=255, verbose_name='推介来源'),
        ),
        migrations.AlterField(
            model_name='recret',
            name='songId',
            field=models.CharField(max_length=255, verbose_name='歌曲Id'),
        ),
    ]
