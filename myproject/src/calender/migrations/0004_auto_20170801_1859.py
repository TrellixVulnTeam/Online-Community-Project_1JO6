# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 22:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0003_auto_20170731_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='studio_calendar',
            name='teacher',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='studio_calendar',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 1, 22, 59, 50, 498958, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
