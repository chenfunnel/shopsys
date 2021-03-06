# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 05:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('cardid', models.CharField(max_length=30, verbose_name='身份证号')),
                ('telephont', models.CharField(max_length=30, verbose_name='手机')),
                ('weixin', models.CharField(max_length=50, verbose_name='微信号')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('sex', models.BooleanField(choices=[(0, '男'), (1, '女')], max_length=1, verbose_name='性别')),
                ('description', models.TextField(verbose_name='描述')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='新增时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'db_table': 'contact',
                'ordering': ['-create_at'],
                'verbose_name_plural': '联系人',
                'verbose_name': '联系人',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('loginname', models.CharField(max_length=30, verbose_name='登录名')),
                ('password', models.CharField(max_length=30, verbose_name='密码')),
                ('telephont', models.CharField(max_length=30, verbose_name='手机')),
                ('weixin', models.CharField(max_length=50, verbose_name='微信号')),
                ('description', models.TextField(verbose_name='描述')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('regist_at', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'db_table': 'customer',
                'ordering': ['-regist_at'],
                'verbose_name_plural': '客户',
                'verbose_name': '客户',
            },
        ),
        migrations.AddField(
            model_name='contact',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regist.Customer'),
        ),
    ]
