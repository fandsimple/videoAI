# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2020-02-08 17:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spiderTask', '0025_recret_isreced'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recret',
            old_name='songIdList',
            new_name='songId',
        ),
    ]
