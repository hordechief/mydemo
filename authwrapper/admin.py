from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session




class PermissionAdmin(admin.ModelAdmin):
    list_display = ["content_type", "name", "codename"]
    list_filter = ["content_type"]
    class Meta:
        model = Permission

class ContentTypeAdmin(admin.ModelAdmin):
    list_display = ["app_label", "model"]
    class Meta:
        model = ContentType

class SessionAdmin(admin.ModelAdmin):
    list_display = ["session_key","expire_date" ,"session_data", ]
    class Meta:
        model = Session

    list_per_page = 10
    list_max_show_all = 20

admin.site.register(Permission, PermissionAdmin)
admin.site.register(ContentType, ContentTypeAdmin)
admin.site.register(Session, SessionAdmin)
