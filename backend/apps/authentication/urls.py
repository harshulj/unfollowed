from django.conf.urls import url, patterns

from .views import twitter_auth_init, twitter_auth_callback, logout


urlpatterns = patterns('',
    url(r'^twitter/$', twitter_auth_init, name='twitter_auth_init'),
    url(r'^twitter_cb/$', twitter_auth_callback, name='twitter_auth_cb'),
    url(r'^logout/$', logout, name='logout'),
)
