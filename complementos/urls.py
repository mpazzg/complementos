from django.conf.urls import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'complementos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^',include('complementos.apps.home.urls')),
    url(r'^',include('complementos.apps.ventas.urls')),
    url(r'^',include('complementos.apps.webServices.wsProductos.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
