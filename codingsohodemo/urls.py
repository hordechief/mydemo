from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import pgwshow

urlpatterns = [
    url(r'^pgwshow/$', pgwshow, name='demo_pgwshow'), 
]