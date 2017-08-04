# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170804_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.AddField(
            model_name='tag',
            name='post',
            field=models.ManyToManyField(related_name='tags', to='blog.Post'),
        ),
    ]
