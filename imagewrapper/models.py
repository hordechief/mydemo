# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from plugin.fields import ThumbnailImageField

def upload_avatar(instance, filename):
    return 'upload/avatar/' + filename

# Create your models here.
class Avatar(models.Model):
    image = ThumbnailImageField(verbose_name=_('Image'), thumb_width=256, thumb_height=256, add_thumb=True, blank=False, null=False, upload_to=upload_avatar)

    class Meta:
        verbose_name = _("avatar")
        verbose_name_plural = _("avatar")

    # def __unicode__(self):
    #     return self.id

    def get_absolute_url(self):
        return reverse("avatar_detail", kwargs={"pk": self.pk })  
   