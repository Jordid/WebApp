from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import get_object_or_404,render_to_response,redirect
from apps.app.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from apps.app import iniciar_sesion, cerrar_sesion, menu, permiso_requerido
# Create your views here.

#------------ Cliente ---------------
def clientes(request):	
	permiso_requerido(request)
	menuLista = menu(request)
	clientes = Cliente.objects.filter(estadoCliente="Activo")
	template = 'formVerClientes.html'
	return render(request, template, {'clientes': clientes, "listaMenu": menuLista})

def nuevo_cliente(request):
	if permiso_requerido:
		menuLista = menu(request)
		lstProvincia = Provincia.objects.all()
		lstCiudad = Ciudad.objects.all()
		lstCiudad2 = Ciudad.objects.filter(provinciaCiudad = lstProvincia[0])
		template = 'formRegistroClientes.html'
		return render(request, template, {"listaMenu": menuLista, 'lstProvincia': lstProvincia, 'lstCiudad': lstCiudad, 'lstCiudad2': lstCiudad2})
	

def editar_cliente(request, cliente_id):
	menuLista = menu(request)
	clienteSelec = Cliente.objects.get(id=cliente_id)	
	lstProvincia = Provincia.objects.all()
	lstCiudad = Ciudad.objects.all()
	idPro = clienteSelec.personaCliente.ciudadPersona.provinciaCiudad.id
	lstCiudad2 = Ciudad.objects.filter(provinciaCiudad = idPro)
	template = 'formActualizarClientes.html'
	return render(request, template, {"listaMenu": menuLista, 'lstProvincia': lstProvincia, 
		'lstCiudad': lstCiudad, 'lstCiudad2': lstCiudad2, 'clienteSelec': clienteSelec})

def eliminar_cliente(request, cliente_id):
	menuLista = menu(request)
	clienteSelec = Cliente.objects.get(id=cliente_id)
	clienteSelec.estadoCliente = "Inactivo"
	clienteSelec.save()
	return redirect('clientes')

def guardar_cliente(request, cliente_id):
	template = ""
	opcion = int(str(cliente_id))
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


#------------ Factura ---------------
def facturas(request):
	menuLista = menu(request)
	lstFactura = Factura.objects.all()
	template = 'formVerFacturas.html'
	return render(request, template, {"listaMenu": menuLista, "lstFactura": lstFactura})

def nuevo_factura(request):
	lstProducto = Producto.objects.all()
	lstCliente = Cliente.objects.all();
	template = 'formRegistroFacturas.html'
	return render(request, template, {"listaMenu": menu(request), "lstCliente":lstCliente,"lstProducto":lstProducto})

def editar_factura(request, factura_id):
	menuLista = menu(request)
	clienteSelec = Cliente.objects.get(id=factura_id)	
	lstProvincia = Provincia.objects.all()
	lstCiudad = Ciudad.objects.all()
	idPro = clienteSelec.personaCliente.ciudadPersona.provinciaCiudad.id
	lstCiudad2 = Ciudad.objects.filter(provinciaCiudad = idPro)
	template = 'formActualizarClientes.html'
	return render(request, template, {"listaMenu": menuLista, 'lstProvincia': lstProvincia, 
		'lstCiudad': lstCiudad, 'lstCiudad2': lstCiudad2, 'clienteSelec': clienteSelec})

def eliminar_factura(request, factura_id):
	menuLista = menu(request)
	clienteSelec = Cliente.objects.get(id=factura_id)
	clienteSelec.estadoCliente = "Inactivo"
	clienteSelec.save()
	return redirect('clientes')

def guardar_factura(request):
	clienteCed = request.GET['cliente'] 
	datosempresa = DatosEmpresa.objects.all()
	dato = datosempresa[0]
	perAux = Persona.objects.get(cedulaPersona=clienteCed)
	cliente = Cliente.objects.get(personaCliente = perAux)
	
	facAux = Factura()
	facAux.numeroFactura = request.GET['numeroFactura']
	facAux.fechaFactura = request.GET['fecha']
	facAux.subtotalFactura = request.GET['subtotal']
	facAux.descuentoFactura = request.GET['descuento']
	facAux.ivaCeroFactura = request.GET['ivaCero']
	facAux.ivaDoceFactura = request.GET['ivaDoce']
	facAux.totalFactura = request.GET['total']
	facAux.estadoFactura = "PENDIENTE"
	facAux.observacionesFactura = request.GET['observaciones']
	facAux.datosEmpresaFactura = dato
	facAux.clienteFactura = cliente
	facAux.save()
	print("Hola :)")

def guardar_detalle(request):
	print("ite 1")
	numeroFac = request.GET['numeroFactura'] 
	print("ite 1")
	productoId = request.GET['productoId']
	print("ite 1")
	factura = Factura.objects.get(numeroFactura = numeroFac)
	print("ite 1")
	producto = Producto.objects.get(id = productoId)
	print("ite 1")
	print("ite 1")
	detFac = DetalleFactura()
	print('Jamaas dire nunca')
	detFac.cantidadDetalleFactura = request.GET['cantidad']
	print('Ok')
	detFac.precioDetalleFactura = request.GET['precio']
	print('Ok1')
	detFac.facturaDetalleFactura = factura
	print('Ok2')
	detFac.productoDetalleFactura = producto
	facAux.save()
	print("Hola :D")
#-------------------------------------
