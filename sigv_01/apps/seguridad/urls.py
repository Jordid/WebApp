from django.conf.urls import patterns, include, url

urlpatterns = patterns('',    

 	url(r'^usuario/lista$', 'apps.seguridad.views.usuarios', name='usuarios'),
 	url(r'^usuario/nuevo$', 'apps.seguridad.views.nuevo_usuario', name='nuevo_usuario'),
 	url(r'^usuario/editar/(\d+)$', 'apps.seguridad.views.editar_usuario', name='editar_usuario'),
 	url(r'^usuario/eliminar/(\d+)$', 'apps.seguridad.views.eliminar_usuario', name='eliminar_usuario'),
 	url(r'^usuario/guardar/(\d+)$', 'apps.seguridad.views.guardar_usuario', name='guardar_usuario'),

    url(r'^rol/lista$', 'apps.seguridad.views.roles', name='roles'),
)
