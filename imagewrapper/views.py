# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.conf import settings
from PIL import Image
import os
from .models import Avatar
from .forms import AvatarForm

# Create your views here.
def avatar_upload(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AvatarForm()
    return render(request, 'avatar_upload.html', {'form': form})

def get_file_path(filename):
    if filename:        
        photoname = os.path.join("upload", "avatar", filename)
        photodir = os.path.join(settings.MEDIA_ROOT, "upload", "avatar")
        if not os.path.exists(photodir):
            os.makedirs(photodir)
        photopath = os.path.join(settings.MEDIA_ROOT, photoname)
        return photoname, photopath
    return None, None
        

class AvatarCreateView(CreateView):
    template_name = 'avatar_upload.html'
    form_class = AvatarForm
    success_url = "/"

    def get_context_data(self, *args, **kwargs):
        context = super(AvatarCreateView, self).get_context_data(*args, **kwargs)
        context["image_form"] = AvatarForm()
        return context

    def post(self, request, *args, **kwargs):        

        if 1:
            filename=request.FILES['image']
            print (filename, 0)
            photoname, photopath = get_file_path(filename.name)
            if photopath:
                img=Image.open(filename)
                img.save(photopath)
                Avatar.objects.create(image = photoname)
                return HttpResponseRedirect('/')

        else:
            imageForm = self.form_class(request.POST, request.FILES)
            if imageForm.is_valid():
                image = imageForm.save(commit=False)
                # add your code here
                image.save()
                return HttpResponseRedirect('/')
            else:
                print imageForm.errors

        return super(AvatarCreateView, self).post(request, *args, **kwargs)    

class AvatarUpdateView(UpdateView):
    template_name = 'avatar_upload.html'
    form_class = AvatarForm
    # success_url = "/"
    model = Avatar

    def get_context_data(self, *args, **kwargs):
        context = super(AvatarUpdateView, self).get_context_data(*args, **kwargs)
        context["image_form"] = AvatarForm(
            instance=self.get_object(), 
            initial={"image":self.get_object().image},
            data={"image":self.get_object().image}
        )

        return context

    def get_success_url(self, *args, **kwargs):
        return self.object.get_absolute_url()

class AvatarDetailView(DetailView):
    template_name = 'avatar_detail.html'
    model = Avatar    