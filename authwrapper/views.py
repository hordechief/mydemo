from django.conf import settings
from django.contrib.auth import authenticate#, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import auth
from django.views.generic.edit import FormView, UpdateView
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from authwrapper.wechat.views import wechat_auth_login

default_redirect_url = settings.LOGIN_REDIRECT_URL or '/'
REDIRECT_FIELD_NAME = 'next'

# below method is also OK
def auth_login_post(request):        
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request=request, username=username, password=password)
    if user is not None:
        auth_login(request, user) 
    else:
        return redirect(reverse("auth_login", kwargs={}))

# Create your views here.
def login(request):
    return wechat_auth_login(request)

def logout(request):
    try:
        del request.session['wechat_id']
    except:
        pass
    auth_logout(request)
    return redirect(default_redirect_url)

def auth_view_login(request):
    return auth_views.login(request, 
          template_name='auth/registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          # authentication_form=AuthenticationForm,
          extra_context=None)




