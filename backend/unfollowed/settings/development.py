from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'unfollowed',
            'USER': 'unfollowed',
            'PASSWORD': 'password',
            'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
            'PORT': '3306',
            }
        }


