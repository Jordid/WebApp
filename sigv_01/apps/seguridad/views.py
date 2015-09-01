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
	lstUsuarios = Usuario.objects.all()
	template = 'formVerUsuarios.html'
	return render(request, template, {"listaMenu": menu(request), "lstUsuarios": lstUsuarios})

def nuevo_usuario(request):
	lstProvincia = Provincia.objects.all()
	lstCiudad = Ciudad.objects.all()
	lstCiudad2 = Ciudad.objects.filter(provinciaCiudad = lstProvincia[0])
	lstRol = Rol.objects.all()
	lstPersona = Persona.objects.all().exclude(cedulaPersona = "0000000000")
	lstUsuario = Usuario.objects.all()
	template = 'formRegistroUsuarios.html'
	return render(request, template, {"listaMenu": menu(request), 
		'lstProvincia': lstProvincia, 'lstCiudad': lstCiudad,
		 'lstCiudad2': lstCiudad2, 'lstRol':lstRol, 'lstPersona':lstPersona,
		 'lstUsuario':lstUsuario})

def editar_usuario(request, usuario_id):
	usuarioSelec = Usuario.objects.get(id=usuario_id)	
	lstProvincia = Provincia.objects.all()
	lstRolEsta = UsuarioRoles.objects.values_list('rolUsuarioRoles', flat=True).filter(usuarioUsuarioRoles=usuarioSelec)
	lstRol = Rol.objects.all()
	lstCiudad = Ciudad.objects.all()
	lstUsuario = Usuario.objects.all()
	idPro = usuarioSelec.personaUsuario.ciudadPersona.provinciaCiudad.id
	lstCiudad2 = Ciudad.objects.filter(provinciaCiudad = idPro)
	template = 'formActualizarUsuarios.html'
	return render(request, template, {"listaMenu": menu(request), 
		'lstProvincia': lstProvincia, 'lstCiudad': lstCiudad, 
		'lstCiudad2': lstCiudad2, 'usuarioSelec': usuarioSelec, 
		'lstRol':lstRol, 'lstUsuario':lstUsuario, 
		'lstRolEsta':lstRolEsta})

def eliminar_usuario(request, usuario_id):
	usuarioSelec = Usuario.objects.get(id=usuario_id)
	usuarioSelec.estadoUsuario = "Inactivo"
	usuarioSelec.save()
	return redirect('usuarios')

def guardar_usuario(request):
	print("Llego :Ok")
	per = Persona()
	usu = Usuario()
	cedula = request.GET['cedula'] 
	ciu = Ciudad(pk = request.GET['ciudadId'])
	existeP = False; existeU = False
	try:
		per = Persona.objects.get(cedulaPersona=cedula)
		existeP = True
		usu = Usuario.objects.get(personaUsuario=per)
		existeU = True;
	except:
		print("No hay persona o usuario")

	per.cedulaPersona = request.GET["cedula"]
	per.apellidosPersona = request.GET["apellidos"]
	per.nombresPersona = request.GET["nombres"]
	per.telefonoPersona =request.GET ["telefono"]
	per.direccionPersona =request.GET["direccion"]
	per.emailPersona =request.GET["email"]
	per.ciudadPersona = ciu
	per.save()
	estado="Activo"
	print("Person save")
	if existeP==False:
		per = Persona.objects.get(cedulaPersona=cedula)
	if existeU==True:
		estado = request.GET['estado']
		UsuarioRoles.objects.filter(usuarioUsuarioRoles=usu).delete()
		print("Borro!")

	usu.estadoUsuario = estado
	usu.nickUsuario = request.GET["nick"]
	usu.claveUsuario = request.GET["clave"]
	usu.personaUsuario = per
	usu.save()	
	print("usuario guardado!")

def guardar_usuario_rol(request):
	usuAux = Usuario.objects.get( nickUsuario= request.GET['nick'])
	rolAux = Rol.objects.get(pk=request.GET['rolId'])
	usuRolAux = UsuarioRoles()
	usuRolAux.usuarioUsuarioRoles = usuAux
	usuRolAux.rolUsuarioRoles = rolAux
	usuRolAux.save()
	print("Hola :) UsuarioRol Guardado!")

"""
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
"""
#------------ Rol ---------------
def roles(request):
	lstRol = Rol.objects.all()
	template = 'formVerRoles.html'
	return render(request, template, {"listaMenu": menu(request), "lstRol": lstRol})

def nuevo_rol(request):
	lstProvincia = Provincia.objects.all()
	lstMenu = Menu.objects.filter(estadoMenu="Activo")
	template = 'formRegistroRoles.html'
	return render(request, template, {"listaMenu": menu(request), 
		'lstMenu': lstMenu})

def editar_rol(request, rol_id):
	rolSelec = Rol.objects.get(pk=rol_id)	
	lstPermisos = Permisos.objects.values_list('menuPermiso', flat=True).filter(rolPermiso = rolSelec)
	lstMenu = Menu.objects.filter(estadoMenu="Activo")
	template = 'formActualizarRoles.html'
	return render(request, template, {"listaMenu": menu(request), 
		'lstPermisos': lstPermisos, 'lstMenu': lstMenu, 'rolSelec':rolSelec})

def guardar_rol(request):
	rolAux = Rol(nombreRol = request.GET['rol'])
	rolAux.save()
	print("Hola :) Rol guardaado!")

def guardar_rol_editar(request):
	rolAux = Rol.objects.get(pk=request.GET['rolID'])
	rolAux.nombreRol = request.GET['nombre']
	rolAux.save()
	Permisos.objects.filter(rolPermiso=rolAux).delete()
	print("Hola :) Rol editado Guardado!")


def guardar_permiso(request):
	print("Hola :) Permiso 1!")
	rolAux = Rol.objects.get(nombreRol = request.GET['rol'])
	print("Hola :) Permiso 2!")
	menuAux = Menu.objects.get(pk=request.GET['idMenu'])
	print("Hola :) Permiso 3!")
	permisoAux = Permisos()
	print("Hola :) Permiso 4!")
	permisoAux.rolPermiso = rolAux
	print("Hola :) Permiso 5!")
	permisoAux.menuPermiso = menuAux
	permisoAux.save()
	print("Hola :) Permiso Guardado!")
#-------------------------------------



