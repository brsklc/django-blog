# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170802_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
