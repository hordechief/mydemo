# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-09 01:30
from __future__ import unicode_literals

import crowdfundings.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Crowdfunding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[(b'health', b'Health'), (b'school', b'School')], max_length=45)),
                ('title', models.CharField(max_length=120)),
                ('detail', models.TextField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=0, default=100, max_digits=50)),
                ('deadline', models.DateTimeField(default=django.utils.timezone.now, verbose_name='deadline')),
                ('is_favorite', models.BooleanField(default=False, help_text='Designates whether this is favorite.', verbose_name='favorite status')),
                ('image', models.ImageField(upload_to=crowdfundings.models.image_upload_to)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
