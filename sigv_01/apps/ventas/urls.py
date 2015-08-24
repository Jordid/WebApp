from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^cliente/lista$', 'apps.ventas.views.clientes', name='clientes'),
	url(r'^cliente/nuevo$', 'apps.ventas.views.nuevo_cliente', name='nuevo_cliente'),
	url(r'^cliente/editar/(\d+)$', 'apps.ventas.views.editar_cliente', name='editar_cliente'),
	url(r'^cliente/eliminar/(\d+)$', 'apps.ventas.views.eliminar_cliente', name='eliminar_cliente'),
	url(r'^cliente/guardar/(\d+)$', 'apps.ventas.views.guardar_cliente', name='guardar_cliente'),
	
	url(r'^factura/lista$', 'apps.ventas.views.facturas', name='facturas'),
	url(r'^factura/nuevo$', 'apps.ventas.views.nuevo_factura', name='nuevo_factura'),
	url(r'^factura/editar/(\d+)$', 'apps.ventas.views.editar_factura', name='editar_factura'),
	url(r'^factura/eliminar/(\d+)$', 'apps.ventas.views.eliminar_factura', name='eliminar_factura'),
	url(r'^factura/guardar$', 'apps.ventas.views.guardar_factura', name='guardar_factura'),

)
