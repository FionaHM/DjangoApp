# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 15:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('snippet', models.CharField(max_length=200)),
                ('created_at', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
