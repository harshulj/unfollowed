from django.conf import settings
from django.conf.urls import patterns, include, url, static
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'unfollowed.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('apps.authentication.urls'))
)
# static files will be served at /
urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

index_url = "/static/index.html"
urlpatterns += patterns('',
    url(r'^/?$', RedirectView.as_view(url=index_url, permanent=False)),
)