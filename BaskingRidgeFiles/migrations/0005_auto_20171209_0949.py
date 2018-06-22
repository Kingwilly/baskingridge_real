# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-09 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaskingRidgeFiles', '0004_auto_20171209_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu_entry',
            name='menu_order',
        ),
        migrations.AlterField(
            model_name='menu_entry',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Menu Order'),
        ),
    ]