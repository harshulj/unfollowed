"""
Django settings for unfollowed project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '28gs)pt)(=)q1!2=p6d#xo%e9oa8f1+=e&qh9efab5#7u!wswx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'apps.authentication',
        'apps.social',
        'rest_framework'
        )

MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        )

ROOT_URLCONF = 'unfollowed.urls'

WSGI_APPLICATION = 'unfollowed.wsgi.application'


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



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


#AUTH_USER_MODEL = 'authentication.SocialUser'
OAUTH_URLS = {
    "twitter" : {
        "request_token" : "https://api.twitter.com/oauth/request_token",
        "authenticate"  : "https://api.twitter.com/oauth/authenticate",
        "access_token"  : "https://api.twitter.com/oauth/access_token"
    }
}

APP_CREDENTIALS = {
    "twitter" : {
        "key" : "2thk9BzFT10uUkwtr68qxyiBB",
        "secret" : "bBn52W8c4E4mQN4dq8UTautewS2oC6QoBw0A93mlNuDPafgrmi"
    }
}

SPA_INDEX = STATIC_URL+"index.html"