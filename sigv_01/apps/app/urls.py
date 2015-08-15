from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
	url(r'^$', 'apps.app.views.home', name='home'),
	url(r'^quienes_somos/$', 'apps.app.views.quienes_somos', name='quienes_somos'),
	url(r'^nuestros_productos/$', 'apps.app.views.nuestros_productos', name='nuestros_productos'),
	url(r'^contactos/$', 'apps.app.views.contactos', name='contactos'),
    url(r'^login/$', 'apps.app.views.login', name='login'),
    url(r'^logout/$', 'apps.app.views.logout', name='logout'),
)