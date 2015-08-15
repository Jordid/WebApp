from django.conf.urls import patterns, include, url

urlpatterns = patterns('',    

 	url(r'^producto/lista$', 'apps.inventario.views.productos', name='productos'),
    url(r'^producto/nuevo$', 'apps.inventario.views.nuevo_producto', name='nuevo_producto'),
    url(r'^producto/editar/(\d+)$', 'apps.inventario.views.editar_producto', name='editar_producto'),
    url(r'^producto/guardar/(\d+)$', 'apps.inventario.views.guardar_producto', name='guardar_producto'),
    url(r'^producto/eliminar/(\d+)$', 'apps.inventario.views.eliminar_producto', name='eliminar_producto'),

    url(r'^kardex/lista$', 'apps.inventario.views.kardex', name='kardex'),

    url(r'^categoria/lista$', 'apps.inventario.views.categorias', name='categorias'),
    url(r'^categoria/nuevo$', 'apps.inventario.views.nuevo_categoria', name='nuevo_categoria'),
    url(r'^categoria/editar/(\d+)$', 'apps.inventario.views.editar_categoria', name='editar_categoria'),
    url(r'^categoria/guardar/(\d+)$', 'apps.inventario.views.guardar_categoria', name='guardar_categoria'),
)
