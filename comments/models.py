# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from mptt.models import MPTTModel, TreeForeignKey
from django_comments.models import Comment

class MPTTComment(MPTTModel, Comment):
    """ Threaded comments - Add support for the parent comment store and MPTT traversal"""
    # a link to comment that is being replied, if one exists
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        # comments on one level will be ordered by date of creation
        order_insertion_by=['submit_date']

    class Meta:
        ordering=['tree_id','lft']
        #app_label = 'comments' 
        '''
        If a model is defined outside of an application in INSTALLED_APPS, it must declare which app it belongs to:

        if not set, it will report below error: 

        mptt\models.py:263: RemovedInDjango19Warning: Model class comments.models.MPTTComment doesn't declare an explicit app_label 
        and ether isn't in an application in INSTALLED_APPS or else was imported before its application was loaded. This will no longer be supported in Django 1.9.
          cls = super_new(meta, class_name, bases, class_dict)

        '''