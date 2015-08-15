from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import get_object_or_404,render_to_response,redirect
from apps.app.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from apps.app import iniciar_sesion, cerrar_sesion, menu
# Create your views here.


#------------ Usuario ---------------
def usuarios(request):
	lstUsuarios = Usuario.objects.filter(estadoUsuario='Activo')
	template = 'formVerUsuarios.html'
	return render(request, template, {"listaMenu": menu(request), "lstUsuarios": lstUsuarios})

def nuevo_usuario(request):
	lstProvincia = Provincia.objects.all()
	lstCiudad = Ciudad.objects.all()
	lstCiudad2 = Ciudad.objects.filter(provinciaCiudad = lstProvincia[0])
	template = 'formRegistroUsuarios.html'
	return render(request, template, {"listaMenu": menu(request), 
		'lstProvincia': lstProvincia, 'lstCiudad': lstCiudad,
		 'lstCiudad2': lstCiudad2})

def editar_usuario(request, usuario_id):
	usuarioSelec = Usuario.objects.get(id=usuario_id)	
	lstProvincia = Provincia.objects.all()
	lstCiudad = Ciudad.objects.all()
	idPro = usuarioSelec.personaUsuario.ciudadPersona.provinciaCiudad.id
	lstCiudad2 = Ciudad.objects.filter(provinciaCiudad = idPro)
	template = 'formActualizarUsuarios.html'
	return render(request, template, {"listaMenu": menu(request), 
		'lstProvincia': lstProvincia, 'lstCiudad': lstCiudad, 
		'lstCiudad2': lstCiudad2, 'usuarioSelec': usuarioSelec})

def eliminar_usuario(request, usuario_id):
	usuarioSelec = Usuario.objects.get(id=usuario_id)
	usuarioSelec.estadoUsuario = "Inactivo"
	usuarioSelec.save()
	return redirect('usuarios')

def guardar_usuario(request, usuario_id):
	template = ""
	opcion = int(str(usuario_id))
	if opcion == 0:
		template = "formRegistroUsuarios.html"
	else:
		template = "formActualizarUsuarios.html"
	if request.POST:
		ciu = Ciudad()
		per = Persona()
		usu = Usuario()
		estado = "Activo"
		if opcion != 0:
			estado = request.POST["estado"]
			per= Persona.objects.get(cedulaPersona=request.POST["cedula"])
			usu= Usuario.objects.get(id = usuario_id)
		
		ciu.id = request.POST["selectbasicC"]
		per.cedulaPersona = request.POST["cedula"]
		per.apellidosPersona = request.POST["apellidos"]
		per.nombresPersona = request.POST["nombres"]
		per.telefonoPersona =request.POST ["telefono"]
		per.direccionPersona =request.POST["direccion"]
		per.emailPersona =request.POST["email"]
		per.ciudadPersona = ciu
		per.save()

		perAux = Persona.objects.get(cedulaPersona=request.POST["cedula"])
		usu.estadoUsuario = estado
		usu.nickUsuario = request.POST["nick"]
		usu.claveUsuario = request.POST["clave"]
		usu.personaUsuario = perAux
        usu.save()
        return redirect('usuarios')
	returnnse(template,context_instance=RequestContext(request, locals()))
#-------------------------------------

#------------ Rol ---------------
def roles(request):
	lstRol = Rol.objects.all()
	template = 'formVerRoles.html'
	return render(request, template, {"listaMenu": menu(request), "lstRol": lstRol})
#-------------------------------------



