from django.conf.urls import url, patterns

from .views import current_user

urlpatterns = patterns('',
    url(r'^user/$', current_user, name='current_user'),
)
