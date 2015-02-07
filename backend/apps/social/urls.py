from django.conf.urls import url, patterns

from .views import current_user

urlpatterns = patterns('',
    url(r'^v1/users/$', current_user, name='current_user'),
)
