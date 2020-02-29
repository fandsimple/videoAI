# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2020-02-15 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiderTask', '0031_auto_20200209_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountRet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='员工姓名')),
                ('startTime', models.TimeField(verbose_name='上班时间')),
                ('endTime', models.TimeField(verbose_name='下班时间')),
                ('couldStartTime', models.TimeField(null=True, verbose_name='规定上班时间')),
                ('couldEndTime', models.TimeField(null=True, verbose_name='规定下班时间')),
                ('dec', models.CharField(default='', max_length=255, verbose_name='出勤描述')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '出勤记录表',
                'db_table': 'countret',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='姓名')),
                ('age', models.IntegerField(default=33, verbose_name='年龄')),
                ('phone', models.CharField(default='', max_length=255, verbose_name='手机号')),
                ('sex', models.CharField(choices=[('男', '男'), ('女', '女')], max_length=10, verbose_name='性别')),
                ('img', models.ImageField(upload_to='emplyeePic/', verbose_name='本人头像')),
                ('jobTime', models.DateTimeField(auto_now=True, verbose_name='入职时间')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '员工信息表',
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='JobConf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='标题')),
                ('startTime', models.TimeField(verbose_name='工作开始时间')),
                ('endTime', models.TimeField(verbose_name='工作结束时间')),
                ('isSelect', models.CharField(default='0', max_length=10, verbose_name='是否生效')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '上下班时间配置表',
                'db_table': 'jobconf',
            },
        ),
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='名字')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '零时打卡记录',
                'db_table': 'temp',
            },
        ),
        migrations.DeleteModel(
            name='Playlist',
        ),
        migrations.DeleteModel(
            name='RecderAlter',
        ),
        migrations.DeleteModel(
            name='RecRetAlter',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
