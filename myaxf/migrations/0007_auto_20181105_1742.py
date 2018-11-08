# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-05 17:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myaxf', '0006_auto_20181105_1002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(default=1)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_selected', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '购物车',
            },
        ),
        migrations.AlterField(
            model_name='goods',
            name='childcidname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='goods',
            name='dealerid',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='goods',
            name='marketprice',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='goods',
            name='pmdesc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='goods',
            name='productimg',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='goods',
            name='productlongname',
            field=models.CharField(max_length=190),
        ),
        migrations.AlterField(
            model_name='goods',
            name='productname',
            field=models.CharField(max_length=130),
        ),
        migrations.AlterField(
            model_name='goods',
            name='productnum',
            field=models.IntegerField(verbose_name='销量'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='specifics',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='goods',
            name='storenums',
            field=models.IntegerField(verbose_name='库存'),
        ),
        migrations.AddField(
            model_name='cart',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myaxf.Goods'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterIndexTogether(
            name='cart',
            index_together=set([('user', 'goods')]),
        ),
    ]
