# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_auto_20170310_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippets',
            name='snippet',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='snippets',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
