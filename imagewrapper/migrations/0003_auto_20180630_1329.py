# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-30 05:29
from __future__ import unicode_literals

from django.db import migrations
import imagewrapper.models
import plugin.fields


class Migration(migrations.Migration):

    dependencies = [
        ('imagewrapper', '0002_auto_20180630_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=plugin.fields.ThumbnailImageField(upload_to=imagewrapper.models.upload_avatar, verbose_name='Image'),
        ),
    ]
