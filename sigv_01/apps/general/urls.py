from django.conf.urls import patterns, include, url

urlpatterns = patterns('',    

 	url(r'^provincia/lista$', 'apps.general.views.provincias', name='provincias'),

    url(r'^ciudad/lista$', 'apps.general.views.ciudades', name='ciudades'),

    url(r'^notificacion/lista$', 'apps.general.views.notificaciones', name='notificaciones'),
    url(r'^notificacion/nuevo$', 'apps.general.views.nuevo_notificacion', name='nuevo_notificacion'),
    url(r'^notificacion/enviar$', 'apps.general.views.enviar_notificacion', name='enviar_notificacion'),

    url(r'^empleado/lista$', 'apps.general.views.empleados', name='empleados'),
    url(r'^empleado/nuevo$', 'apps.general.views.nuevo_empleado', name='nuevo_empleado'),
    url(r'^empleado/editar/(\d+)$', 'apps.general.views.editar_empleado', name='editar_empleado'),
    url(r'^empleado/eliminar/(\d+)$', 'apps.general.views.eliminar_empleado', name='eliminar_empleado'),
    url(r'^empleado/guardar/(\d+)$', 'apps.general.views.guardar_empleado', name='guardar_empleado'),

    url(r'^proveedor/lista$', 'apps.general.views.proveedores', name='proveedores'),
    url(r'^proveedor/nuevo$', 'apps.general.views.nuevo_proveedor', name='nuevo_proveedor'),
    url(r'^proveedor/editar/(\d+)$', 'apps.general.views.editar_proveedor', name='editar_proveedor'),
    url(r'^proveedor/eliminar/(\d+)$', 'apps.general.views.eliminar_proveedor', name='eliminar_proveedor'),
    url(r'^proveedor/guardar/(\d+)$', 'apps.general.views.guardar_proveedor', name='guardar_proveedor'),

)
