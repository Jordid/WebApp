from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import get_object_or_404,render_to_response,redirect
from apps.app.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from apps.app import iniciar_sesion, cerrar_sesion, menu
from apps.general import enviar_email
# Create your views here.


#------------ Provincia --------------------------
def provincias(request):
	lstProvincia = Provincia.objects.all()
	template = 'formVerProvincias.html'
	return render(request, template, {"listaMenu": menu(request), 'lstProvincia': lstProvincia})

def nuevo_provincia(request):
	provinciaSelec = Provincia(id=0)
	lstProvincia = Provincia.objects.all()
	template = 'formRegistroProvincias.html'
	return render(request, template, {"listaMenu": menu(request),
	 'lstProvincia': lstProvincia, 'provinciaSelec':provinciaSelec})

def editar_provincia(request, provincia_id):
	provinciaSelec = Provincia.objects.get(id=provincia_id)
	lstProvincia = Provincia.objects.all()
	template = 'formRegistroProvincias.html'
	return render(request, template, {"listaMenu": menu(request), 'lstProvincia': lstProvincia, 
		'provinciaSelec': provinciaSelec})

def eliminar_provincia(request, provincia_id):
	Provincia.objects.get(id=provincia_id).delete()
	return redirect('provincias')

def guardar_provincia(request, provincia_id):
	template = "formRegistroProvincias.html"
	opcion = int(str(provincia_id))

	if request.POST:
		pro = Provincia()

		if opcion != 0:
			try:
				pro = Provincia.objects.get(pk=provincia_id)
			except:
				print("No hay provincia")
		pro.nombreProvincia = request.POST["descripcion"]
		pro.save()
        print("Elemento guardado!")
        return redirect('provincias')
	returnnse(template,context_instance=RequestContext(request, locals()))
#-------------------------------------------------

#------------ Ciudad ---------------
def ciudades(request):
	lstCiudad = Ciudad.objects.all()
	template = 'formVerCiudades.html'
	return render(request, template, {"listaMenu": menu(request), 'lstCiudad': lstCiudad})

def nuevo_ciudad(request):
	ciudadSelec = Ciudad(id=0)
	lstCiudad = Ciudad.objects.all()
	lstProvincia = Provincia.objects.all()
	template = 'formRegistroCiudades.html'
	return render(request, template, {"listaMenu": menu(request),
		'lstProvincia': lstProvincia, 'ciudadSelec':ciudadSelec, 'lstCiudad':lstCiudad})

def editar_ciudad(request, ciu_id):
	ciudadSelec = Ciudad.objects.get(id=ciu_id)
	lstCiudad = Ciudad.objects.all()
	lstProvincia = Provincia.objects.all()
	template = 'formRegistroCiudades.html'
	return render(request, template, {"listaMenu": menu(request), 'lstProvincia': lstProvincia, 
		'ciudadSelec': ciudadSelec, 'lstCiudad':lstCiudad})

def eliminar_ciudad(request, ciudad_id):
	Ciudad.objects.get(id=ciudad_id).delete()
	return redirect('ciudades')

def guardar_ciudad(request, ciudad_id):
	template = "formRegistroCiudades.html"
	opcion = int(str(ciudad_id))

	if request.POST:
		ciu = Ciudad()
		pro = Provincia(pk = request.POST["selectbasicP"])
		if opcion != 0:
			try:
				ciu = Ciudad.objects.get(pk=ciudad_id)
			except:
				print("No hay ciudad")
		ciu.provinciaCiudad = pro
		ciu.nombreCiudad = request.POST["descripcion"]
		ciu.save()
        print("Elemento guardado!")
        return redirect('ciudades')
	returnnse(template,context_instance=RequestContext(request, locals()))

#-------------------------------------

#------------ Notificaciones ---------------
def notificaciones(request):
	lstNotificacion = Notificacion.objects.all()
	template = 'formVerNotificaciones.html'
	return render(request, template, {"listaMenu": menu(request), 'lstNotificacion': lstNotificacion})

def nuevo_notificacion(request):
	lstCliente = Cliente.objects.all()
	lstAviso = Aviso.objects.all()
	lstclienteAtrasados = clientes_atrasados()
	template = 'formGenerarNotificaciones.html'
	return render(request, template, {"listaMenu": menu(request), 'lstCliente': lstCliente, 
		'lstAviso':lstAviso, "lstclienteAtrasados":lstclienteAtrasados})

#-------------------------------------
def clientes_atrasados( ):
	lstCuenta = CuentaCobrar.objects.filter(estadoCuentaCobrar="Atrasado")
	lstCliente =[]
	for cue in lstCuenta:
		if cue.clienteCuentaCobrar is not lstCliente:
			lstCliente.append(cue.clienteCuentaCobrar)
	return lstCliente

#------------ Empleado -------------------------
def empleados(request):
	lstEmpleado = Empleado.objects.filter(estadoEmpleado="Activo")
	template = 'formVerEmpleados.html'
	return render(request, template, {"listaMenu": menu(request), 'lstEmpleado': lstEmpleado})

def nuevo_empleado(request):
	lstProvincia = Provincia.objects.all()
	lstCiudad = Ciudad.objects.all()
	lstCiudad2 = Ciudad.objects.filter(provinciaCiudad = lstProvincia[0])
	lstPersona = Persona.objects.all().exclude(cedulaPersona = "0000000000")
	lstEmpleado = Empleado.objects.all()
	template = 'formRegistroEmpleados.html'
	return render(request, template, {"listaMenu": menu(request),
	 'lstProvincia': lstProvincia, 'lstCiudad': lstCiudad,
	  'lstCiudad2': lstCiudad2, 'lstPersona':lstPersona,
	  'lstEmpleado':lstEmpleado})

def editar_empleado(request, empleado_id):
	empleadoSelec = Empleado.objects.get(id=empleado_id)	
	lstProvincia = Provincia.objects.all()
	lstCiudad = Ciudad.objects.all()
	idPro = empleadoSelec.personaEmpleado.ciudadPersona.provinciaCiudad.id
	lstCiudad2 = Ciudad.objects.filter(provinciaCiudad = idPro)
	lstPersona = Persona.objects.all().exclude(cedulaPersona = "0000000000")
	template = 'formActualizarEmpleados.html'
	return render(request, template, {"listaMenu": menu(request), 'lstProvincia': lstProvincia, 
		'lstCiudad': lstCiudad, 'lstCiudad2': lstCiudad2, 'empleadoSelec': empleadoSelec,
		'lstPersona':lstPersona})

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

		cedula = request.POST["cc_ruc"] 
		ciu = Ciudad(pk = request.POST['selectbasicC'])
		existeP = False; existeE = False
		if opcion == 0:
			try:
				per = Persona.objects.get(cedulaPersona=cedula)
				existeP = True
				emp = Empleado.objects.get(personaEmpleado=per)
				existeE = True;
			except:
				print("No hay persona o empleado")
		else:
			try:
				emp = Empleado.objects.get(pk=empleado_id)
				existeE = True;
				per = Persona.objects.get(pk=emp.personaEmpleado.id)
				existeP = True
			except:
				print("No hay persona o empleado 2")

		per.cedulaPersona = cedula
		per.apellidosPersona = request.POST["apellidos"]
		per.nombresPersona = request.POST["nombres"]
		per.telefonoPersona =request.POST ["telefono"]
		per.direccionPersona =request.POST["direccion"]
		per.emailPersona =request.POST["email"]
		per.ciudadPersona = ciu
		per.save()
		print("person save")
		estado = "Activo"
		if existeP==False:
			per = Persona.objects.get(cedulaPersona=cedula)
		if existeE==True:
			estado = request.POST['estado']

		emp.estadoEmpleado = estado
		emp.cargoEmpleado = request.POST["cargo"]
		emp.observacionesEmpledo = request.POST["observaciones"]
		emp.personaEmpleado = per
        emp.save()
        print("Empleado guardado!")
        return redirect('empleados')
	returnnse(template,context_instance=RequestContext(request, locals()))
#---------------------------------------------------

#------------ Proveedor ---------------------------
def proveedores(request): 
	lstProveedor = Proveedor.objects.filter(estadoProveedor="Activo")
	template = 'formVerProveedores.html'
	return render(request, template, {"listaMenu": menu(request), 'lstProveedor': lstProveedor})

def nuevo_proveedor(request):
	lstProvincia = Provincia.objects.all()
	lstCiudad = Ciudad.objects.all()
	lstPersona = Persona.objects.all().exclude(cedulaPersona = "0000000000")
	lstProveedor = Proveedor.objects.all()
	lstCiudad2 = Ciudad.objects.filter(provinciaCiudad = lstProvincia[0])
	template = 'formRegistroProveedores.html'
	return render(request, template, {"listaMenu": menu(request),
	 'lstProvincia': lstProvincia, 'lstCiudad': lstCiudad,
	  'lstCiudad2': lstCiudad2, 'lstPersona':lstPersona,
	  'lstProveedor':lstProveedor})

def editar_proveedor(request, proveedor_id):
	proveedorSelec = Proveedor.objects.get(id=proveedor_id)	
	lstProvincia = Provincia.objects.all()
	lstCiudad = Ciudad.objects.all()
	idPro = proveedorSelec.personaProveedor.ciudadPersona.provinciaCiudad.id
	lstCiudad2 = Ciudad.objects.filter(provinciaCiudad = idPro)
	lstPersona = Persona.objects.all().exclude(cedulaPersona = "0000000000")
	template = 'formActualizarProveedores.html'
	return render(request, template, {"listaMenu": menu(request), 'lstProvincia': lstProvincia, 
		'lstCiudad': lstCiudad, 'lstCiudad2': lstCiudad2, 'proveedorSelec': proveedorSelec,
		'lstPersona':lstPersona})

def eliminar_proveedor(request, proveedor_id):
	proveedorSelec = Proveedor.objects.get(id=proveedor_id)
	proveedorSelec.estadoProveedor = "Inactivo"
	proveedorSelec.save()
	return redirect('proveedores')

def guardar_proveedor(request, pro_id):
	template = ""
	opcion = int(str(pro_id))
	if opcion == 0:
		template = "formRegistroProveedores.html"
	else:
		template = "formActualizarProveedores.html"

	if request.POST:
		ciu = Ciudad()
		per = Persona()
		pro = Proveedor()

		cedula = request.POST["cc_ruc"] 
		ciu = Ciudad(pk = request.POST['selectbasicC'])
		existeP = False; existeE = False
		if opcion == 0:
			try:
				per = Persona.objects.get(cedulaPersona=cedula)
				existeP = True
				print("OK")
				print(per.id)
				pro = Proveedor.objects.get(personaProveedor=per)
				existeE = True;
			except:
				print("No hay persona o empleado")
		else:
			try:
				pro = Proveedor.objects.get(pk=pro_id)
				existeE = True;
				per = Persona.objects.get(pk=pro.personaProveedor.id)
				existeP = True
			except:
				print("No hay persona o proveedor 2")

		per.cedulaPersona = cedula
		per.apellidosPersona = request.POST["apellidos"]
		per.nombresPersona = request.POST["nombres"]
		per.telefonoPersona =request.POST ["telefono"]
		per.direccionPersona =request.POST["direccion"]
		per.emailPersona =request.POST["email"]
		per.ciudadPersona = ciu
		per.save()
		print("person save")
		estado = "Activo"
		if existeP==False:
			per = Persona.objects.get(cedulaPersona=cedula)
		if existeE==True:
			estado = request.POST['estado']

		pro.estadoProveedor = estado
		pro.observacionesProveedor = request.POST["observaciones"]
		pro.personaProveedor = per
		pro.save()
        print("Elemento guardado!")
        return redirect('proveedores')
	returnnse(template,context_instance=RequestContext(request, locals()))

def enviar_notificacion(request):
	lstclienteAtrasados = clientes_atrasados()
	for cli in lstclienteAtrasados:
		enviar_email("","","Asunto", "Mensaje", cli.personaCliente.emailPersona )
	return redirect('nuevo_notificacion')

#---------------------------------------------------

#------------ Datos Empresa --------------- 
def datos_empresa(request): 
	dato = DatosEmpresa.objects.all()[0]
	lstProvincia = Provincia.objects.all()
	lstCiudad = Ciudad.objects.all()
	idPro = dato.ciudadDatosEmpresa.provinciaCiudad.id
	lstCiudad2 = Ciudad.objects.filter(provinciaCiudad = idPro)
	template = 'formActualizarDatosEmpresa.html'
	return render(request, template, {"listaMenu": menu(request), 'dato': dato, 
		'lstProvincia':lstProvincia, 'lstCiudad':lstCiudad, 'lstCiudad2':lstCiudad2})

def guardar_datos_empresa(request):
	dato = DatosEmpresa.objects.all()[0]
	ciu = Ciudad.objects.get(pk = request.POST["selectbasicC"])
	dato.nombreDatosEmpresa = request.POST["nombre"]
	dato.direccionDatosEmpresa = request.POST["direccion"]
	dato.telefonoDatosEmpresa = request.POST["telefono"]
	dato.misionDatosEmpresa = request.POST["mision"]
	dato.visionDatosEmpresa = request.POST["vision"]
	dato.nuestrosProductosDatosEmpresa = request.POST["nuestros"]
	dato.quienesSomosDatosEmpresa = request.POST["quienessomos"]
	dato.logoDatosEmpresa = request.POST["logo"]
	dato.emailDatosEmpresa = request.POST["email"]
	dato.claveDatosEmpresa = request.POST["clave"] 
	dato.ciudadDatosEmpresa = ciu
	dato.save()
	print("Save Data Enterprise!")
	return redirect('datos_empresa')



