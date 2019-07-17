from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.core.urlresolvers import reverse_lazy
from django.contrib import admin
from django.contrib.auth import views as auth_views

from .sms import (
    get_otp, 
    )

from .views import (
    RegistrationView, 
    UserProfileListView, 
    UserProfileUpdateView,
    UserProfileDetailView,
    UserProfileDetailUpdateImageView,
    RegistrationForgetView
    )


urlpatterns = [
    # opt code    
    url(r'^getVerificationCode/$', get_otp, name='getVerificationCode'), 

    # user create / update
    url(r'^register/$', RegistrationView.as_view(), name='register_phone'),     
    url(r'^user/(?P<pk>\d+)/edit$', UserProfileUpdateView.as_view(), name='userprofile_update'), 
    url(r'^user/(?P<pk>\d+)$', UserProfileDetailView.as_view(), name='userprofile_detail'), 
    url(r'^user/(?P<pk>\d+)/edit/avatar$', UserProfileDetailUpdateImageView.as_view(), name='userprofile_detail_update_avatar'), 
    url(r'^user/$', UserProfileListView.as_view(), name='userprofile_list'),     

    # password
    url(r'^password/change/$', auth_views.password_change, 
                {'post_change_redirect': reverse_lazy('auth_password_change_done2')}, name='auth_password_change2'), 
    url(r'^password/change/done/$', auth_views.password_change_done, name='auth_password_change_done2'), 
    url(r'^password/forget/$', RegistrationForgetView.as_view(), name='authwrapper_password_forget'),     

    # url(r'^phone_login/', include('phone_login.urls')),
]
