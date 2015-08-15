from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.app.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sigv_01.views.home', name='home'),
	url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.app.urls')),
    url(r'^contable/',include('apps.contable.urls')),
    url(r'^general/',include('apps.general.urls')),
    url(r'^inventario/',include('apps.inventario.urls')),
    url(r'^seguridad/',include('apps.seguridad.urls')),
    url(r'^ventas/',include('apps.ventas.urls')),

)
