# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-11 18:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TwinBrooksUser', '0003_auto_20170204_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='access_level',
        ),
        migrations.RemoveField(
            model_name='user',
            name='flagged',
        ),
    ]
