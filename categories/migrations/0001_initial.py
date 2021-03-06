# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-30 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Название')),
                ('menu_title', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Текст ссылки')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]
