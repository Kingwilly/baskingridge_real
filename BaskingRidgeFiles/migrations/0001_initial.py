# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-16 01:08
from __future__ import unicode_literals

import BaskingRidgeFiles.models
from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gallery_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(null=True, upload_to=BaskingRidgeFiles.models.upload_image)),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
            ],
            options={
                'verbose_name': 'Gallery Image',
                'verbose_name_plural': 'Gallery Images',
            },
        ),
        migrations.CreateModel(
            name='menu_entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=255)),
                ('menu_pdf', models.FileField(null=True, upload_to=BaskingRidgeFiles.models.upload_image)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Menu Description')),
            ],
            options={
                'verbose_name': 'Menu Entry',
                'verbose_name_plural': 'Menu Entries',
            },
        ),
    ]