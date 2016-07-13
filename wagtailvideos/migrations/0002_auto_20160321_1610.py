# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-21 05:10
from __future__ import unicode_literals

import wagtailvideos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailvideos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to=wagtailvideos.models.get_upload_to, verbose_name='file'),
        ),
    ]
