
from django.contrib.auth import get_user_model
from authwrapper.wechat.models import WechatUserProfile
from django.conf import settings

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

UserModel = get_user_model()

class AuthwrapperMiddleware(MiddlewareMixin):

    def process_request(self, request):

        try:                  
            request.register_type = settings.ACCOUNT_REGISTER_TYPE
                  
            if request.user.is_anonymous:
                   from django.utils.module_loading import import_string
                   backend = import_string('authwrapper.backends.auth.WechatBackend')()
                   request.wechat = backend.get_wechat_user(request)
        except:
            pass
