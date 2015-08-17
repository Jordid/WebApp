from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import get_object_or_404,render_to_response,redirect
from apps.app.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from apps.app import menu
# Create your views here.

#------------ CuentaCobrar ---------------
def cuentas_por_cobrar(request):
	lstCuentaCobrar = CuentaCobrar.objects.all()
	template = 'formVerCuentasPorCobrar.html'
	return render(request, template, {"listaMenu": menu(request), "lstCuentaCobrar": lstCuentaCobrar})
#-------------------------------------


#------------ CuentaPagar ---------------
def cuentas_por_pagar(request):
	lstCuentaPagar = CuentaPagar.objects.all()
	template = 'formVerCuentasPorPagar.html'
	return render(request, template, {"listaMenu": menu(request), "lstCuentaPagar": lstCuentaPagar})
#-------------------------------------