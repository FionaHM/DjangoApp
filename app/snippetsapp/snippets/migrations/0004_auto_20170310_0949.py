# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20170309_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippets',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='snippets',
            name='snippet',
            field=models.TextField(max_length=300),
        ),
    ]
