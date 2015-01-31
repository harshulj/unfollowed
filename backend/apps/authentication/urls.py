from django.conf.urls import url, patterns

from .views import request_token


urlpatterns = patterns('',
    url(r'^request_token/$', request_token, name='request_token'),
)
