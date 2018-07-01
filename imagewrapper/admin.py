# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Avatar

# Register your models here.
class AvatarAdmin(admin.ModelAdmin):
    list_display = ["id", "image",]

    view_on_site = False

    class Meta:
        model = Avatar

admin.site.register(Avatar, AvatarAdmin)    