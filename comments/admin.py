# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import MPTTComment

class MPTTCommentAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'parent',  
        # 'site',
        'user',
        # 'user_name',
        # 'user_email',
        # 'user_url',
        'content_type',
        'object_pk',
        'content_object',
        'comment',
        # '__unicode__',         
    ]

    list_editable = [
        # 'comment',
    ]

    class Meta:
        model = MPTTComment

admin.site.register(MPTTComment, MPTTCommentAdmin)