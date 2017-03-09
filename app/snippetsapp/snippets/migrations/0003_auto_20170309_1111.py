# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 17:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20170308_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippets',
            name='updated_at',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='snippets',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='snippets',
            name='snippet',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='snippets',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
