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

def guardar_usuario_nuevo(request):
	contador = request.GET['contador']
	print("contador: " + str(contador))
	cedula = request.GET["cedula"]
	print(cedula)
	
	if str(contador)=="1":
		p = Persona.objects.filter(cedulaPersona=request.GET['cedula']).count()
		print("------->CANTIDAD DE personas"+str(p))
		ciu = Ciudad.objects.get(pk = request.GET['ciudadId'])
		print("Mi ciudad es " + ciu.nombreCiudad)
		if p == 0:
			per = Persona(
				cedulaPersona=request.GET["cedula"],
				apellidosPersona=request.GET["apellidos"],
				nombresPersona=request.GET["nombres"],
				telefonoPersona=request.GET ["telefono"],
				direccionPersona=request.GET["direccion"],
				emailPersona=request.GET["email"],
				ciudadPersona=ciu
				)
			per.save()
		else:
			per = Persona.objects.get(cedulaPersona=request.GET["cedula"])
			per.cedulaPersona = request.GET["cedula"]
			per.apellidosPersona = request.GET["apellidos"]
			per.nombresPersona = request.GET["nombres"]
			per.telefonoPersona =request.GET ["telefono"]
			per.direccionPersona =request.GET["direccion"]
			per.emailPersona =request.GET["email"]
			per.ciudadPersona = ciu
			per.save()
			usu = Usuario(
				estadoUsuario="Activo",
				nickUsuario=request.GET["nick"],
				claveUsuario=request.GET["clave"],
				personaUsuario=per)
			usu.save()	
			print("usuario guardado!")
	usuAux = Usuario.objects.get(nickUsuario= request.GET['nick'])
	print("Hola")
	rolAux = Rol.objects.get(pk=request.GET['rolId'])
	usuRolAux = UsuarioRoles(
		usuarioUsuarioRoles=usuAux,
		rolUsuarioRoles=rolAux
		)
	usuRolAux.save()


def guardar_usuario_editar(request):
	contador = request.GET['contador']
	print("contador: " + str(contador))
	cedula = request.GET["cedula"]
	print(cedula)
	
	per = Persona.objects.get(pk=request.GET["idPersona"])
	usuAux=Usuario.objects.get(pk= request.GET['idUsuario'])
	if str(contador)=="1":
		ciu = Ciudad.objects.get(pk = request.GET['ciudadId'])
		print("Mi ciudad es " + ciu.nombreCiudad)
		per.cedulaPersona = request.GET["cedula"]
		per.apellidosPersona = request.GET["apellidos"]
		per.nombresPersona = request.GET["nombres"]
		per.telefonoPersona =request.GET ["telefono"]
		per.direccionPersona =request.GET["direccion"]
		per.emailPersona =request.GET["email"]
		per.ciudadPersona = ciu
		per.save()
		usuAux.estadoUsuario=request.GET["estado"]
		usuAux.nickUsuario=request.GET["nick"]
		usuAux.claveUsuario=request.GET["clave"]
		usuAux.save()
		print("User save!")
		UsuarioRoles.objects.filter(usuarioUsuarioRoles=usuAux).delete()
		print("Borro!")
	print("Hola")
	rolAux = Rol.objects.get(pk=request.GET['rolId'])
	usuRolAux = UsuarioRoles(
		usuarioUsuarioRoles=usuAux,
		rolUsuarioRoles=rolAux
		)
	usuRolAux.save()
	print("guardo rol")

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

def guardar_rol_nuevo(request):
	print("ok mmmmmm")
	contador = request.GET['contador']
	print("contador: " + str(contador))
	miRol = request.GET['rol']
	print("Rol"  +str(miRol))
	if str(contador)=="1":
		rolAux = Rol(
			nombreRol=request.GET['rol']
			)
		rolAux.save()
		
	rolAux = Rol.objects.get(nombreRol = request.GET['rol'])
	menuAux = Menu.objects.get(pk=request.GET['idMenu'])
	permisoAux = Permisos(
		rolPermiso=rolAux,
		menuPermiso=menuAux
		)
	permisoAux.save()
	print("Hola :) Permiso Guardado!")

def guardar_rol_editar(request):
	print("ok mmmmmm")
	contador = request.GET['contador']
	miRol = request.GET['rol']
	rolAux=Rol.objects.get(pk=request.GET['idRol'])
	if str(contador)=="1":
		rolAux.nombreRol=request.GET['rol']
		rolAux.save()
		print("Actualizo rol...")
		Permisos.objects.filter(rolPermiso=rolAux).delete()
	menuAux = Menu.objects.get(pk=request.GET['idMenu'])
	permisoAux = Permisos(
		rolPermiso=rolAux,
		menuPermiso=menuAux
		)
	permisoAux.save()
	print("Hola :) Permiso Guardado!")

def guardar_permiso(request):
	print("Hola :) Permiso 1!")
#-------------------------------------



