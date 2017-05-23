# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 07:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regist', '0005_auto_20170509_1107'),
        ('plan', '0004_auto_20170508_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel_plan',
            name='contact',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='regist.Contact'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='contact',
            field=models.ManyToManyField(to='regist.Contact'),
        ),
        migrations.AddField(
            model_name='plane_plan',
            name='contact',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='regist.Contact'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='train_plan',
            name='contact',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='regist.Contact'),
            preserve_default=False,
        ),
    ]