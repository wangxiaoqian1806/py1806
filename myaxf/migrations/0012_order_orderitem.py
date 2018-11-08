# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-08 10:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import myaxf.models


class Migration(migrations.Migration):

    dependencies = [
        ('myaxf', '0011_myuser_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('staus', models.IntegerField(choices=[(1, '代付款'), (2, '已付款'), (3, '已发货'), (4, '已收货'), (5, '待评价'), (6, '已评价')], default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods', models.IntegerField(verbose_name=myaxf.models.Goods)),
                ('num', models.IntegerField(verbose_name='数量')),
                ('buy_money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myaxf.Order')),
            ],
        ),
    ]
