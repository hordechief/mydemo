
from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import render
from django.core.cache import cache
from django.core.cache.backends.memcached import MemcachedCache
from django.conf import settings
from PIL import Image
import json
import os

from .forms import UploadFileForm

UPLOAD_PATH = 'upload'

def get_upload_path():
    if hasattr(settings, "USE_SAE_BUCKET" ) and settings.USE_SAE_BUCKET: #'SERVER_SOFTWARE' in os.environ: 
        return settings.SAE_BUCKET_UPLOAD_PATH #'upload'
    else:
        photopath = os.path.join(settings.MEDIA_ROOT, UPLOAD_PATH)
        if not os.path.exists(photopath):
            os.makedirs(photopath)
        return photopath

def get_upload_url():
    photopath = os.path.join(settings.MEDIA_URL, UPLOAD_PATH)
    return photopath    

# Create your views here.
def upload_file(request):
    if request.method == 'POST':
        upload_form = UploadFileForm(request.POST, request.FILES)
        if upload_form.is_valid():
            in_mem_image_file=request.FILES['image']
            filepath = os.path.join(get_upload_path(), in_mem_image_file.name)
            if in_mem_image_file:
                if hasattr(settings, "USE_SAE_BUCKET" ) and settings.USE_SAE_BUCKET: #'SERVER_SOFTWARE' in os.environ: 
                    from saewrapper.storage.bucket import SAEBucket
                    SAEBucket().put_object(filepath,in_mem_image_file.file.getvalue())
                else:
                    img = Image.open(in_mem_image_file)                          
                    img.save(filepath)
                cache.set('cache_key_upload', os.path.join(UPLOAD_PATH, in_mem_image_file.name) ,60*15)
            return HttpResponse(json.dumps({'message': 'Upload complete!','url': os.path.join(get_upload_url(), in_mem_image_file.name)}))
        else:
            return HttpResponse(json.dumps({'message': 'invalid form!'}))
    else:
        form = UploadFileForm()
        #return render_to_response('index.html', {'form': form}, context_instance=RequestContext(request))
        return HttpResponse(json.dumps({'message': 'invalid form!'}))

def upload_status(request):
    if request.method == 'GET':
        if request.GET['key']:
            csrftoken = request.META.get("CSRF_COOKIE") if "CSRF_COOKIE" in request.META else None
            cache_exist = cache.get(csrftoken)
            request_csrftoken = request.GET['key']
            match = True
            try:
                from django.middleware.csrf import _sanitize_token, _compare_salted_tokens
                request_csrftoken = _sanitize_token(request_csrftoken)                
                match = _compare_salted_tokens(request_csrftoken, csrftoken)
            except:
                pass
            if cache_exist and match:
                value = cache.get(csrftoken)
                return HttpResponse(json.dumps(value), content_type="application/json")
            elif not _compare_salted_tokens(key, csrftoken):
                return HttpResponse(json.dumps({'error':"csrf value not match"}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({'error':"No csrf value in cache"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'error':'No parameter key in GET request'}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'error':'No GET request'}), content_type="application/json")