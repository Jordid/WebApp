from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import get_object_or_404,render_to_response,redirect
from apps.app.models import *
from django.http import HttpResponse,HttpResponseRedirect
from clases import MenuCabecera
from django.contrib.auth.decorators import login_required
from apps.app import iniciar_sesion, cerrar_sesion, menu
# Create your views here.

def login(request):
	mensaje = None
	template = "home.html"
	if request.POST:
		inicio_sesion = iniciar_sesion(request)
		if inicio_sesion is not None:
			request.session["usuarioSession"] = inicio_sesion
			return redirect('home')
		else:
			mensaje = "Usuario o clave incorrectos"
	return render(request, template, {"listaMenu": menu(request), "mensaje": mensaje})

def logout(request):
	cerrar_sesion(request)
	return redirect('home')

def home(request):
	template = 'home.html'
	return render(request, template, {"listaMenu": menu(request)})

def quienes_somos(request):
	template = 'about-us.html'
	return render(request, template, {"listaMenu": menu(request)})

def nuestros_productos(request):
	template = 'portfolio.html'
	return render(request, template, {"listaMenu": menu(request)})

def contactos(request):
	template = 'contact-us.html'
	return render(request, template, {"listaMenu": menu(request)})
