from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.cache import cache
from django.contrib.auth import authenticate#, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import auth
from django.views.generic.edit import FormView, UpdateView, FormMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import JsonResponse, Http404
import datetime

from authwrapper.backends import auth as auth_wrapper

from .forms import RegistrationForgetForm, UserUpdateForm, UserUpdateImageForm, UploadFileForm

from django.utils.module_loading import import_string
REGISTRATION_FORM_PATH = getattr(settings, 'REGISTRATION_FORM','authwrapper.phone.forms.RegistrationForm')
REGISTRATION_FORM = import_string(REGISTRATION_FORM_PATH)

from django.contrib.auth import get_user_model
UserModel = get_user_model

default_redirect_url = settings.LOGIN_REDIRECT_URL or '/'

# from django.contrib.auth.models import User
# http://www.cnblogs.com/smallcoderhujin/p/3193103.html

  

class RegistrationView(FormView):
    form_class = REGISTRATION_FORM
    success_url = None
    template_name = 'auth/registration_form.html'

    #def dispatch(self, request, *args, **kwargs):
    #    return super(RegistrationView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        new_user = self.register(form)
        success_url = self.get_success_url(new_user)
        try:
            to, args, kwargs = success_url
        except ValueError:
            return redirect(success_url)
        else:
            return redirect(to, *args, **kwargs)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def register(self, form):
        #{'phone': u'13409876541', 'password': u'123', 'otp': u'123'}
        phone_number = form.cleaned_data['phone']
        form.cleaned_data.pop('otp')

        user = UserModel().objects.filter(
            phone=phone_number
        ).first()  #not active user, user forgetpassword

        if not user:
            user = (UserModel().objects.create_user(
                username = phone_number,
                account_type = 'phone', 
                #**form.cleaned_data))
                is_active = False,
                phone = phone_number,
                password = form.cleaned_data['password']))
        else:
            user.is_active = True
            user.save()

        return user            

    def get_success_url(self, user=None):        
        try:
            return reverse("userprofile_update", kwargs={'pk':user.id}) 
        except:
            return reverse(default_redirect_url) 


class RegistrationForgetView(RegistrationView):
    form_class = RegistrationForgetForm
    template_name = 'auth/registration_form_forget.html'
    success_url = default_redirect_url

    def register(self, form):
        user = super(RegistrationForgetView,self).register(form)
        authenticate(**{'user':user})
        auth_login(self.request, user)

# pk value is in self.kwargs

class UserProfileUpdateView(UpdateView):
    model = UserModel
    form_class = UserUpdateForm
    template_name = 'auth/userprofile_update_form.html'
    success_url = None
    

    def get_object(self, *args, **kwargs):
        try:
            return  UserModel().objects.get(id=self.kwargs.get('pk'))
            #return UserModel._default_manager.get_by_natural_key(self.kwargs.get('pk'))
        except:
            return None


    def get_form(self, form_class=UserUpdateForm):
        kwargs = self.get_form_kwargs()
        kwargs.update({'instance': self.get_object()})
        form = self.form_class(**kwargs)  
        return form

    '''
    def get_form(self,  *args, **kwargs):
        form = super(ProfileUpdateView, self).get_form(*args, **kwargs)
        #form.fields['phone'] = self.get_object(args,kwargs).phone
        return form
    '''
    def post(self, request, *args, **kwargs): 

        self.object = self.get_object()
        form = self.get_form() # use get_form() to replace, it will include all the information
        #form = self.form_class(request.POST, request.FILES,instance=self.get_object())  
        if form.is_valid():            
            user = form.save(commit=False)
            #user.id = self.kwargs.get('pk') # WHY it will create a new object HERE?
            user.is_active = True
            user.save() 

            wechat = auth_wrapper.WechatBackend().get_wechat_user(request)            
            if wechat:
                wechat.user = user   
                wechat.save()

            '''
            wechat_id = self.request.session.get('wechat_id',None)
            if wechat_id:
                wechat = WechatUserProfile.objects.get(pk=wechat_id) 
                wechat.user = user   
                wechat.save()
            '''
            
            auth.authenticate(**{'user':user})
            auth_login(request, user)

            return redirect(reverse("userprofile_detail", kwargs={'pk':self.object.id}) )
        else:
            return self.form_invalid(form) #redirect(reverse("register_phone", kwargs={}))

        return redirect(default_redirect_url)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class UserProfileDetailView(DetailView):
    model = UserModel
    template_name = 'auth/userprofile_detail.html'

    def get_queryset(self, *args, **kwargs):
        return  UserModel().objects.all()

class UserProfileDetailUpdateImageView(FormMixin, DetailView):
    model = UserModel
    template_name = 'auth/userprofile_detail.html'
    form_class = UserUpdateImageForm

    def get_object(self, *args, **kwargs):
        try:
            return  UserModel().objects.get(id=self.kwargs.get('pk'))
            return UserModel._default_manager.get_by_natural_key(self.kwargs.get('pk'))
        except:
            return None

    def get_context_data(self, *args, **kwargs):
        context = super(UserProfileDetailUpdateImageView, self).get_context_data(*args, **kwargs)
        context["form"] = self.form_class(instance = self.get_object())
        context["upload_form"] = UploadFileForm()
        return context

    def get_success_url(self):
        return reverse("userprofile_detail", kwargs=self.kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            usermodel = UserModel().objects.get(id=self.kwargs.get("pk"))

            # method 1 - input upload
            image = None
            if 'image' in form.cleaned_data and form.cleaned_data.get('image'):
                image = form.cleaned_data['image']
            # method 2 - ajax upload
            if cache.has_key('cache_key_upload') and cache.get('cache_key_upload',None):
                image = cache.get('cache_key_upload')
                cache.delete('cache_key_upload')
            if image:
                usermodel.image = image
                usermodel.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class UserProfileListView(ListView):
    model = UserModel
    template_name = 'auth/userprofile_list.html' 

    def get_queryset(self, *args, **kwargs):
        return  UserModel().objects.all()