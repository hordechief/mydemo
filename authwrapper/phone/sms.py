from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect

from phone_login.models import PhoneToken
from phonenumber_field.validators import validate_international_phonenumber as vip

@csrf_exempt
def get_otp(request):
    if request.is_ajax():
        try:
            vip(request.POST['phone_number'])
        except:
            return JsonResponse({"token": None})

        token = PhoneToken.create_otp_for_number(
                    request.POST['phone_number'])
        return JsonResponse({"token": token.otp})
    else:
        return redirect(default_redirect_url)
        raise Http404