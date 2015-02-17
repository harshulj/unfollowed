from django.conf.urls import url, patterns

from .views import user, followers

urlpatterns = patterns('',
    url(r'^v1/users/(?P<user_id>\d+)/followers/$', followers, name='followers' ),
    url(r'^v1/users/(?P<user_id>\d*)/$', user, name='user'),
    url(r'^v1/users/$', user, name='user'),
)
