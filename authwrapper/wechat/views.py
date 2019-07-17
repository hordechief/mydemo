from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate#, login, logout

from weixin.client import WeixinMpAPI
#from weixin.oauth2 import OAuth2AuthExchangeError

from django.contrib.auth import login as auth_login
'''
def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          extra_context=None):
'''
from django.contrib.auth import logout as auth_logout
'''
def logout(request, next_page=None,
           template_name='registration/logged_out.html',
           redirect_field_name=REDIRECT_FIELD_NAME,
           extra_context=None):
'''           
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .models import WechatUserProfile
from authwrapper.backends.auth import WechatBackend

default_redirect_url = settings.LOGIN_REDIRECT_URL or '/'

def wechat_auth_url_request(request):
    #REDIRECT_URI = "http://%s%s" % (request.META['HTTP_HOST'], reverse("login", kwargs={}))
    REDIRECT_URI = request.build_absolute_uri('/').strip("/") + reverse("wechat_auth_login", kwargs={})
    api = WeixinMpAPI(appid=settings.APP_ID, app_secret=settings.APP_SECRET,redirect_uri=REDIRECT_URI)
    redirect_uri = api.get_authorize_login_url(scope=("snsapi_userinfo",))
    return redirect(redirect_uri) #  "GET /zh/authwrapper/weixin/auth_login/?code=081xJ2wf2A2pbJ05JNwf2RPmwf2xJ2wT&state= HTTP/1.1" 302 0



#refer to django/contrib/auth/views.py
#http://127.0.0.1:8000/accounts/activate/??
def wechat_auth_login(request):
    REDIRECT_URI = request.POST.get('next', request.GET.get('next', default_redirect_url)) #next indicated in templaetes

    if request.method == 'GET':
        code = request.GET.get('code')
        if code:
            redirect_to = "http://%s%s" % (request.META['HTTP_HOST'], default_redirect_url) # redirection URL after authenticate
            api = WeixinMpAPI(appid=settings.APP_ID, 
                        app_secret=settings.APP_SECRET,
                        redirect_uri=redirect_to)
            auth_info = api.exchange_code_for_access_token(code=code)
            api = WeixinMpAPI(access_token=auth_info['access_token'])
            api_user = api.user(openid=auth_info['openid']) 
            user = authenticate(request = request, user = api_user)
            if user and not user.is_anonymous():
                auth_login(request, user)
                return redirect(redirect_to)
            else:
                print "authenticate failure, redirect to login page"
        else:
            print "not code in GET request, this is not correct wechat login request, redirect to login page"

        # return redirect(reverse("auth_login", kwargs={})) # registration url
        return redirect(reverse("auth_view_login", kwargs={}))
    else:  # normal login is POST
        REDIRECT_FIELD_NAME = 'next'
        return auth_views.login(request, template_name='auth/registration/login.html', redirect_field_name=REDIRECT_FIELD_NAME, extra_context=None)   

        # below method is also OK
        auth_login_post(request)

    # 
    return auth_views.login(request, redirect_field_name=REDIRECT_URI, extra_context=None)  

@login_required
def account_link_to_wechat(request):
    next_url = request.GET.get('next', None)
    next_url = next_url or default_redirect_url
    user = auth.get_user(request)
    wechat = WechatBackend().get_wechat_user(request)
    if wechat:
        wechat.user = user   
        wechat.save()    
        return redirect(next_url)

    return redirect(next_url)

# @login_required
# def account_unlink_from_wechat(request):
#     wechat = WechatBackend().get_wechat_user(request)
#     if wechat:
#         wechat.user = None   
#         wechat.save()    

#     if request.is_ajax():
#         data = {'unlink' : True }
#         return JsonResponse(data)

#     return redirect(default_redirect_url)    