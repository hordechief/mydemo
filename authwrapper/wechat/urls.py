from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.core.urlresolvers import reverse_lazy
from django.contrib import admin


from authwrapper.wechat.views import (
    wechat_auth_url_request,
    wechat_auth_login,

    account_link_to_wechat,
    # account_unlink_from_wechat,
    )

urlpatterns = [    
    url(r'^auth_url_request/$', wechat_auth_url_request, name='wechat_auth_url_request'), 
    url(r'^auth_login/$', wechat_auth_login, name='wechat_auth_login'),  

    url(r'^linktowechat$', account_link_to_wechat, name='link_to_wechat'),  
    # url(r'^unlinkfromwechat$', account_unlink_from_wechat, name='unlink_from_wechat'),  
]
