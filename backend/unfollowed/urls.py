from django.conf import settings
from django.conf.urls import patterns, include, url, static
from django.contrib import admin
from django.views.generic.base import RedirectView

from common.views import main_router

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('apps.authentication.urls')),
    url(r'^api/', include('apps.social.urls'))
)

urlpatterns += patterns('',
    url(r'^/?$', main_router, name='main_router'),
)

# static files will be served at /
urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

index_url = settings.STATIC_URL + "index.html"

