# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-10-01 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiderTask', '0016_auto_20191001_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxy',
            name='proxyId',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='代理ID'),
        ),
    ]
