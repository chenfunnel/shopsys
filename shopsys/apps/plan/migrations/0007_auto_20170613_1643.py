# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-13 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0006_hotel_plane_train'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='city',
            field=models.CharField(default='北京', max_length=40, verbose_name='城市'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plane',
            name='arrive_at',
            field=models.TimeField(verbose_name='落地时间'),
        ),
        migrations.AlterField(
            model_name='plane',
            name='start_at',
            field=models.TimeField(verbose_name='起飞时间'),
        ),
        migrations.AlterField(
            model_name='plane_plan',
            name='arrive_at',
            field=models.TimeField(verbose_name='落地时间'),
        ),
        migrations.AlterField(
            model_name='plane_plan',
            name='start_at',
            field=models.TimeField(verbose_name='起飞时间'),
        ),
        migrations.AlterField(
            model_name='train',
            name='arrive_at',
            field=models.TimeField(verbose_name='到站时间'),
        ),
        migrations.AlterField(
            model_name='train',
            name='start_at',
            field=models.TimeField(verbose_name='发车时间'),
        ),
        migrations.AlterField(
            model_name='train_plan',
            name='arrive_at',
            field=models.TimeField(verbose_name='到站时间'),
        ),
        migrations.AlterField(
            model_name='train_plan',
            name='start_at',
            field=models.TimeField(verbose_name='发车时间'),
        ),
    ]
