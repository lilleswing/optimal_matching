# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-23 12:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvfile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 8, 23, 12, 59, 1, 100431)),
            preserve_default=False,
        ),
    ]
