# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2020-02-07 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiderTask', '0019_user_liketag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('playlistId', models.AutoField(primary_key=True, serialize=False, verbose_name='歌单Id')),
                ('playlistName', models.CharField(max_length=255, verbose_name='歌单名称')),
                ('playlistTag', models.CharField(max_length=255, verbose_name='歌单分类')),
                ('playlistDec', models.CharField(max_length=255, verbose_name='歌单描述')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '歌单',
                'db_table': 'playlist',
            },
        ),
    ]