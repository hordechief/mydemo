
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from .views import (
    AvatarCreateView,
    AvatarUpdateView,
    AvatarDetailView,
    avatar_upload,
    )


urlpatterns = [
    url(r'^$', AvatarCreateView.as_view(),name="avatar_create"),
    url(r'^(?P<pk>\d+)/edit$', AvatarUpdateView.as_view(),name="avatar_update"),
    url(r'^(?P<pk>\d+)$', AvatarDetailView.as_view(),name="avatar_detail"),
    url(r'^upload$', avatar_upload, name="avatar_upload"),
]
