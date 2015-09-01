from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import get_object_or_404,render_to_response,redirect
from apps.app.models import *
from django.http import HttpResponse,HttpResponseRedirect
from clases import MenuCabecera
from apps.app import iniciar_sesion, cerrar_sesion, menu, permiso_requerido
from io import BytesIO
from cStringIO import StringIO
from reportlab.pdfgen import canvas
# Create your views here.

def hello_pdf(request):
	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=hello.pdf'
	buffer = BytesIO()
	# Create the PDF object, using the StringIO object as its "file."
	p = canvas.Canvas(buffer)
	# Draw things on the PDF. Here's where the PDF generation happens.
	# See the ReportLab documentation for the full list of functionality.
	p.drawString(100, 100, "Hello world.")
	# Close the PDF object cleanly.
	p.showPage()
	p.save()
	# Get the value of the BytesIO buffer and write it to the response.
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response

def login(request):
	mensaje = "Hola"
	template = "home.html"
	if request.POST:
		inicio_sesion = iniciar_sesion(request)
		if inicio_sesion != 0:
			request.session["usuarioSession"] = inicio_sesion
			request.session.set_expiry(3600) #El inicio de sesion expira pasado una hora

			return redirect('/')
		else:
			mensaje = "Usuario o clave incorrectos"
	return render(request, template, {"listaMenu": menu(request), "mensaje": mensaje})

def logout(request):
	cerrar_sesion(request)
	return redirect('/')

def home(request):
	template = "home.html"
	#response = tiene_permiso(request)
	#if response == False:
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

def guardar_persona():
	pass

