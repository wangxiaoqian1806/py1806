# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-06 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaxf', '0009_minebtns'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='minebtns',
            options={'verbose_name': '我的页面的下一排按钮'},
        ),
        migrations.AddField(
            model_name='minebtns',
            name='is_used',
            field=models.BooleanField(default=True, verbose_name='是否在使用'),
        ),
    ]
