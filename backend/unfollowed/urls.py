from django.conf import settings
from django.conf.urls import patterns, include, url, static
from django.contrib import admin

# Static files are being served at root, so they will be the first conf
urlpatterns = static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'unfollowed.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('apps.authentication.urls')),
)
