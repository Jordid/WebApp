from django.conf.urls import patterns, include, url

urlpatterns = patterns('',    

 	url(r'^usuario/lista$', 'apps.seguridad.views.usuarios', name='usuarios'),
 	url(r'^usuario/nuevo$', 'apps.seguridad.views.nuevo_usuario', name='nuevo_usuario'),
 	url(r'^usuario/editar/(\d+)$', 'apps.seguridad.views.editar_usuario', name='editar_usuario'),
 	url(r'^usuario/eliminar/(\d+)$', 'apps.seguridad.views.eliminar_usuario', name='eliminar_usuario'),
 	url(r'^usuario/guardar$', 'apps.seguridad.views.guardar_usuario', name='guardar_usuario'),
 	url(r'^usuariorol/guardar$', 'apps.seguridad.views.guardar_usuario_rol', name='guardar_usuario_rol'),

    url(r'^rol/lista$', 'apps.seguridad.views.roles', name='roles'),
    url(r'^rol/nuevo$', 'apps.seguridad.views.nuevo_rol', name='nuevo_rol'),
    url(r'^rol/guardar$', 'apps.seguridad.views.guardar_rol', name='guardar_rol'),
    url(r'^rol/guardar_editar$', 'apps.seguridad.views.guardar_rol_editar', name='guardar_rol_editar'),
 	url(r'^rol/editar/(\d+)$', 'apps.seguridad.views.editar_rol', name='editar_rol'),
    url(r'^permiso/guardar$', 'apps.seguridad.views.guardar_permiso', name='guardar_permiso'),
)
