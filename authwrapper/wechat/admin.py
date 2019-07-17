from django.contrib import admin

# Register your models here.
from .models import WechatUserProfile


class WechatUserProfileAdmin(admin.ModelAdmin):
    list_display = ["openid", "unionid", "nickname"]
    class Meta:
        model = WechatUserProfile


admin.site.register(WechatUserProfile, WechatUserProfileAdmin)

