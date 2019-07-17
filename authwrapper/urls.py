from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.core.urlresolvers import reverse_lazy
from django.contrib import admin
from django.contrib.auth import views as auth_views

from .views import (
    logout, 
    login,
    auth_view_login,
    )


urlpatterns = [    
    url(r'^logout/$', logout, name='authwrapper_logout'), 
    url(r'^login/$', login, name='authwrapper_login'), 
    url(r'^auth_login/$', auth_view_login, name='auth_view_login'), 

    # default
    url(r'^auth/', include('django.contrib.auth.urls')),
    # registration
    # url(r'^accounts/', include('registration.backends.default.urls')),        
    # wechat
    url(r'^weixin/', include('authwrapper.wechat.urls')),
    # phone
    url(r'^phone/', include('authwrapper.phone.urls')),
]

# if "wechat" in settings.INSTALLED_APPS:
#     from wechat.views import wechatlogin
#     urlpatterns +=  [
#         url(r'^wechatlogin/$', wechatlogin, name='wechatlogin'), 
#     ]


'''
registration/auth_urls.py

from distutils.version import LooseVersion
from django import get_version
from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/$',
        auth_views.login,
        {'template_name': 'registration/login.html'},
        name='auth_login'),
    url(r'^logout/$',
        auth_views.logout,
        {'template_name': 'registration/logout.html'},
        name='auth_logout'),


    url(r'^password/change/$',
        auth_views.password_change,
        {'post_change_redirect': reverse_lazy('auth_password_change_done')},
        name='auth_password_change'),
    url(r'^password/change/done/$',
        auth_views.password_change_done,
        name='auth_password_change_done'),

        
    url(r'^password/reset/$',
        auth_views.password_reset,
        {'post_reset_redirect': reverse_lazy('auth_password_reset_done')},
        name='auth_password_reset'),
    url(r'^password/reset/complete/$',
        auth_views.password_reset_complete,
        name='auth_password_reset_complete'),
    url(r'^password/reset/done/$',
        auth_views.password_reset_done,
        name='auth_password_reset_done'),
]


if (LooseVersion(get_version()) >= LooseVersion('1.6')):
    urlpatterns += [
        url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
            auth_views.password_reset_confirm,
            {'post_reset_redirect': reverse_lazy('auth_password_reset_complete')},
            name='auth_password_reset_confirm')
    ]
else:
    urlpatterns += [
        url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.password_reset_confirm,
            {'post_reset_redirect': reverse_lazy('auth_password_reset_complete')},
            name='auth_password_reset_confirm')
    ]

'''

# django.contrib.auth.urls.py
'''
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^password_change/$', views.password_change, name='password_change'),
    url(r'^password_change/done/$', views.password_change_done, name='password_change_done'),
    url(r'^password_reset/$', views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', views.password_reset_complete, name='password_reset_complete'),
]
'''