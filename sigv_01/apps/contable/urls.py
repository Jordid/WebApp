from django.conf.urls import patterns, include, url

urlpatterns = patterns('',    

 	url(r'^cuenta_por_cobrar/lista$', 'apps.contable.views.cuentas_por_cobrar', name='cuentas_por_cobrar'),
    url(r'^cuenta_por_pagar/lista$', 'apps.contable.views.cuentas_por_pagar', name='cuentas_por_pagar'),

)
