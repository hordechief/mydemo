from django.contrib import admin
from django.contrib.sites.models import Site

class SiteAdmin(admin.ModelAdmin):
    list_display = ["domain","name", ]
    class Meta:
        model = Site

    list_per_page = 10
    list_max_show_all = 20

admin.site.register(Site, SiteAdmin)     