# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-24 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('goods', '0006_remove_goodsbase_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsbase',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.Categories', verbose_name='Категории'),
        ),
    ]
