# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 06:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_plan_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='plan',
            name='hotletype',
            field=models.IntegerField(choices=[(1, '星级宾馆'), (2, '商务宾馆')], verbose_name='住宿'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='ifback',
            field=models.BooleanField(choices=[(1, '是'), (2, '否')], verbose_name='是否往返'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='traffictype',
            field=models.IntegerField(choices=[(1, '飞机'), (2, '高铁'), (3, '普客')], verbose_name='交通工具'),
        ),
    ]