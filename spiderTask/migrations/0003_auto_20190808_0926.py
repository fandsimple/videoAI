# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-08-08 09:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spiderTask', '0002_ip'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ip',
            new_name='Proxy',
        ),
        migrations.AlterModelTable(
            name='proxy',
            table='proxy',
        ),
    ]
