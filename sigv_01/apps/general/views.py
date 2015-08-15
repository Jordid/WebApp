from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import get_object_or_404,render_to_response,redirect
from apps.app.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from apps.app import iniciar_sesion, cerrar_sesion, menu
# Create your views here.


#------------ Provincia ---------------
def provincias(request):
	lstProvincia = Provincia.objects.all()
	template = 'formVerProvincias.html'
	return render(request, template, {"listaMenu": menu(request), 'lstProvincia': lstProvincia})
#-------------------------------------

#------------ Ciudad ---------------
def ciudades(request):
	lstCiudad = Ciudad.objects.all()
	template = 'formVerCiudades.html'
	return render(request, template, {"listaMenu": menu(request), 'lstCiudad': lstCiudad})
#-------------------------------------

#------------ Notificaciones ---------------
def notificaciones(request):
	lstNotificacion = Notificacion.objects.all()
	template = 'formVerNotificaciones.html'
	return render(request, template, {"listaMenu": menu(request), 'lstNotificacion': lstNotificacion})

def nuevo_notificacion(request):
	lstAviso = Aviso.objects.all()
	template = 'formGenerarNotificaciones.html'
	return render(request, template, {"listaMenu": menu(request), 'lstAviso': lstAviso})
#-------------------------------------

#------------ Empleado ---------------
def empleados(request):
	lstEmpleado = Empleado.objects.filter(estadoEmpleado="Activo")
	template = 'formVerEmpleados.html'
	return render(request, template, {"listaMenu": menu(request), 'lstEmpleado': lstEmpleado})

def nuevo_empleado(request):
	lstProvincia = Provincia.objects.all()
	lstCiudad = Ciudad.objects.all()
	lstCiudad2 = Ciudad.objects.filter(provinciaCiudad = lstProvincia[0])
	template = 'formRegistroEmpleados.html'
	return render(request, template, {"listaMenu": menu(request), 'lstProvincia': lstProvincia, 'lstCiudad': lstCiudad, 'lstCiudad2': lstCiudad2})

def editar_empleado(request, empleado_id):
	empleadoSelec = Empleado.objects.get(id=empleado_id)	
	lstProvincia = Provincia.objects.all()
	lstCiudad = Ciudad.objects.all()
	idPro = empleadoSelec.personaEmpleado.ciudadPersona.provinciaCiudad.id
	lstCiudad2 = Ciudad.objects.filter(provinciaCiudad = idPro)
	template = 'formActualizarEmpleados.html'
	return render(request, template, {"listaMenu": menu(request), 'lstProvincia': lstProvincia, 
		'lstCiudad': lstCiudad, 'lstCiudad2': lstCiudad2, 'empleadoSelec': empleadoSelec})

def eliminar_empleado(request, empleado_id):
	empleadoSelec = Empleado.objects.get(id=empleado_id)
	empleadoSelec.estadoEmpleado = "Inactivo"
	empleadoSelec.save()
	return redirect('empleados')

def guardar_empleado(request, empleado_id):
	template = ""
	opcion = int(str(empleado_id))
	if opcion == 0:
		template = "formRegistroEmpleados.html"
	else:
		template = "formActualizarEmpleados.html"

	if request.POST:
		ciu = Ciudad()
		per = Persona()
		emp = Empleado()
		estado = "Activo"
		if opcion != 0:
			estado = request.POST["estado"]
			per= Persona.objects.get(cedulaPersona=request.POST["cedula"])
			emp= Empleado.objects.get(id = empleado_id)
		
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
		emp.estadoEmpleado = estado
		emp.cargoEmpleado = request.POST["cargo"]
		emp.observacionesEmpledo = request.POST["observaciones"]
		emp.personaEmpleado = perAux
        emp.save()
        return redirect('empleados')
	returnnse(template,context_instance=RequestContext(request, locals()))
#-------------------------------------

#------------ Proveedor --------------- by Jordi
def proveedores(request): 
	lstProveedor = Proveedor.objects.all()
	template = 'formVerProveedores.html'
	return render(request, template, {"listaMenu": menu(request), 'lstProveedor': lstProveedor})

def nuevo_proveedor(request):
	lstProvincia = Provincia.objects.all()
	lstCiudad = Ciudad.objects.all()
	lstCiudad2 = Ciudad.objects.filter(provinciaCiudad = lstProvincia[0])
	template = 'formRegistroProveedores.html'
	return render(request, template, {"listaMenu": menu(request), 'lstProvincia': lstProvincia, 'lstCiudad': lstCiudad, 'lstCiudad2': lstCiudad2})

def editar_proveedor(request, proveedor_id):
	proveedorSelec = Proveedor.objects.get(id=proveedor_id)	
	lstProvincia = Provincia.objects.all()
	lstCiudad = Ciudad.objects.all()
	idPro = proveedorSelec.personaCliente.ciudadPersona.provinciaCiudad.id
	lstCiudad2 = Ciudad.objects.filter(provinciaCiudad = idPro)
	template = 'formActualizarProveedores.html'
	return render(request, template, {"listaMenu": menu(request), 'lstProvincia': lstProvincia, 
		'lstCiudad': lstCiudad, 'lstCiudad2': lstCiudad2, 'proveedorSelec': proveedorSelec})

def eliminar_proveedor(request, proveedor_id):
	proveedorSelec = Proveedor.objects.get(id=proveedor_id)
	proveedorSelec.estadoProveedor = "Inactivo"
	proveedorSelec.save()
	return redirect('proveedores')

def guardar_proveedor(request, proveedor_id):
	template = ""
	opcion = int(str(proveedor_id))
	if opcion == 0:
		template = "formRegistroClientes.html"
	else:
		template = "formActualizarClientes.html"

	if request.POST:
		ciu = Ciudad()
		per = Persona()
		cli = Cliente()
		estado = "Activo"
		if opcion != 0:
			estado = request.POST["estado"]
			per= Persona.objects.get(cedulaPersona=request.POST["cedula"])
			cli= Cliente.objects.get(id = cliente_id)
		
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
		cli.estadoCliente = estado
		cli.observacionesCliente = request.POST["observacion"]
		cli.personaCliente = perAux
        cli.save()
        return redirect('clientes')
	returnnse(template,context_instance=RequestContext(request, locals()))
#-------------------------------------


#------------ Notificaciones ---------------
