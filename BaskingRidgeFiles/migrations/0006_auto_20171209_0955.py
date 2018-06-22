# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-09 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaskingRidgeFiles', '0005_auto_20171209_0949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery_image',
            options={'ordering': ['my_order'], 'verbose_name': 'Gallery Image', 'verbose_name_plural': 'Gallery Images'},
        ),
        migrations.AddField(
            model_name='gallery_image',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Image Order'),
        ),
    ]
