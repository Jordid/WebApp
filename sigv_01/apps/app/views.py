from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import get_object_or_404,render_to_response,redirect
from apps.app.models import *
from django.http import HttpResponse,HttpResponseRedirect
from clases import MenuCabecera
from apps.app import iniciar_sesion, cerrar_sesion, menu, permiso_requerido
# Create your views here.

def login(request):
	mensaje = "Hola"
	template = "home.html"
	if request.POST:
		inicio_sesion = iniciar_sesion(request)
		if inicio_sesion != 0:
			request.session["usuarioSession"] = inicio_sesion
			return redirect('/')
		else:
			mensaje = "Usuario o clave incorrectos"
	return render(request, template, {"listaMenu": menu(request), "mensaje": mensaje})

def logout(request):
	cerrar_sesion(request)
	return redirect('/')

def home(request):
	template = "home.html"
	if request.session.get('usuarioSession') is None:
		request.session['usuarioSession'] = 3
	response = tiene_permiso(request)
	if response == False:
		response = render(request, "home.html", {"listaMenu": menu(request)})
	return response

def quienes_somos(request):
	dato = DatosEmpresa.objects.all()[0]
	template = 'about-us.html'
	return render(request, template, {"listaMenu": menu(request), 'dato': dato})

def nuestros_productos(request):
	template = 'portfolio.html'
	return render(request, template, {"listaMenu": menu(request)})

def contactos(request):
	template = 'contact-us.html'
	return render(request, template, {"listaMenu": menu(request)})

def tiene_permiso(request):
	template = '404.html'
	if permiso_requerido(request) == False:
		return render(request, template, {"listaMenu": menu(request)})
	else:
		return False
def fecha(request):
	template = 'fecha.html'
	return render(request, template)

