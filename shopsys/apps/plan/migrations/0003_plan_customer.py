# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 02:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regist', '0002_auto_20170414_1042'),
        ('plan', '0002_auto_20170502_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='regist.Customer'),
            preserve_default=False,
        ),
    ]
