# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-05 10:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myaxf', '0005_goods_goodstypes_mainshow'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GoodsTypes',
            new_name='FoodsTypes',
        ),
    ]
