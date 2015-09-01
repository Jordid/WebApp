from django.conf.urls import patterns, include, url

urlpatterns = patterns('',    
 	url(r'^cuenta_por_cobrar/lista$', 'apps.contable.views.cuentas_por_cobrar', name='cuentas_por_cobrar'),
 	url(r'^cuenta_por_cobrar/nuevo$', 'apps.contable.views.nuevo_cuenta_por_cobrar', name='nuevo_cuenta_por_cobrar'),
 	url(r'^cuenta_por_cobrar/guardar$', 'apps.contable.views.guardar_cuenta_por_cobrar', name='guardar_cuenta_por_cobrar'),
 	url(r'^cuenta_por_cobrar/guardarDetalle$', 'apps.contable.views.guardar_detalle_cuenta_por_cobrar', name='guardar_detalle_cuenta_por_cobrar'),
 	url(r'^cuenta_por_cobrar/abonar/insertar$', 'apps.contable.views.insertar_abono_cuenta_por_cobrar', name='insertar_abono_cuenta_por_cobrar'),
 	url(r'^cuenta_por_cobrar/abonar/eliminar$', 'apps.contable.views.eliminar_abono_cuenta_por_cobrar', name='eliminar_abono_cuenta_por_cobrar'),
	url(r'^cuenta_por_cobrar/vista/(\d+)$', 'apps.contable.views.vista_cuenta_por_cobrar', name='vista_cuenta_por_cobrar'),
	url(r'^cuenta_por_cobrar/abonar/(\d+)$', 'apps.contable.views.abonar_cuenta_por_cobrar', name='abonar_cuenta_por_cobrar'),
    url(r'^cuenta_por_pagar/lista$', 'apps.contable.views.cuentas_por_pagar', name='cuentas_por_pagar'),
)
