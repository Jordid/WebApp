from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^cliente/lista$', 'apps.ventas.views.clientes', name='clientes'),
	url(r'^cliente/nuevo$', 'apps.ventas.views.nuevo_cliente', name='nuevo_cliente'),
	url(r'^cliente/editar/(\d+)$', 'apps.ventas.views.editar_cliente', name='editar_cliente'),
	url(r'^cliente/eliminar/(\d+)$', 'apps.ventas.views.eliminar_cliente', name='eliminar_cliente'),
	url(r'^cliente/guardar/(\d+)$', 'apps.ventas.views.guardar_cliente', name='guardar_cliente'),
	
	url(r'^factura/lista$', 'apps.ventas.views.facturas', name='facturas'),
	url(r'^factura/nuevo$', 'apps.ventas.views.nuevo_factura', name='nuevo_factura'),
	url(r'^factura/enviar/(\d+)$', 'apps.ventas.views.enviar_factura', name='enviar_factura'),
	url(r'^factura/anular/(\d+)$', 'apps.ventas.views.anular_factura', name='anular_factura'),
	url(r'^factura/guardar$', 'apps.ventas.views.guardar_factura', name='guardar_factura'),
	url(r'^factura/guardarDetalle$', 'apps.ventas.views.guardar_detalle', name='guardar_detalle'),

)
