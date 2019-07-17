"""
Django settings for mydemo project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yp(774_irv-#xb!+esvm$8a7j=&88y91_r!bekei*_^r_t$_zj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    # 'django.contrib.flatpages', 

    'django_comments', 
    'mptt',    
    'comments',
        
    'authwrapper',
    'authwrapper.phone',
    'authwrapper.wechat',
    'phone_login',
    'rest_framework',
    'rest_framework.authtoken',    
    'crispy_forms',
    'weixin',

    'imagewrapper',
    'codingsohodemo',
    'fileuploadwrapper',
    'plugin',
    

    'crowdfundings'
]

COMMENTS_APP = 'comments'

MIDDLEWARE = [
    'authwrapper.middleware.AuthwrapperMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mydemo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [            
            os.path.join(BASE_DIR, "plugin", "templates"),
            os.path.join(BASE_DIR, "comments", "templates"),
            os.path.join(BASE_DIR, "templates"),  
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                # 'django.contrib.auth.context_processors.PermWrapper',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mydemo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
TIME_ZONE = 'Asia/Shanghai'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "static_root")
STATIC_ROOT = os.path.join(BASE_DIR, "static_in_env", "static_root")
    
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_in_pro", "our_static"),
    # os.path.join(BASE_DIR, "imagewrapper", "static"), 
    # os.path.join(os.path.dirname(BASE_DIR), "env", "Lib", "site-packages", "django", "contrib", "admin", "static"),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "static_in_env", "media_root")



# auth

ACCOUNT_ALLOW_MIX_TYPE_LOGIN = True
UUSLUGIFY = True

AUTHENTICATION_BACKENDS = (        
    'authwrapper.backends.auth.MyBackend', 
    'authwrapper.backends.auth.WechatBackend',     
    # 'phone_login.backends.phone_backend.PhoneBackend',
    'django.contrib.auth.backends.ModelBackend',    
    )
AUTH_USER_MODEL = 'phone.MyUser'

ACCOUNT_REGISTER_TYPE =  'phone' #phone, 'mail',

# Wechat
if not 'SERVER_SOFTWARE' in os.environ:
    APP_ID = 'wxe90ebbe29377e650' #changyubingfeng
    APP_SECRET = 'd4624c36b6795d1d99dcf0547af5443d'    
else:
    APP_ID = 'wx168434ba37e8c17b' #
    APP_SECRET = 'd4624c36b6795d1d99dcf0547af5443d'

APP_ID = 'wx5700620c309d157e'
APP_SECRET = 'e9cae7ab69f641c6e4c793457c04cad4'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

# Configure the SENDSMS_BACKEND (for django-sendsms integration)
# SENDSMS_BACKEND = 'myapp.mysmsbackend.SmsBackend' #(defaults to 'sendsms.backends.console.SmsBackend')
SENDSMS_FROM_NUMBER = "+XXxxxxxxxxxx" 
SENDSMS_ACCOUNT_SID = 'ACXXXXXXXXXXXXXX'
SENDSMS_AUTH_TOKEN = 'xxxxxxxx' 

PHONE_LOGIN_ATTEMPTS = 100

LOGIN_REDIRECT_URL = '/'

SITE_ID = 1

from django.conf import global_settings
FILE_UPLOAD_HANDLERS = ['fileuploadwrapper.uploadfilehandler.UploadProgressCachedHandler', ] \
+ global_settings.FILE_UPLOAD_HANDLERS

