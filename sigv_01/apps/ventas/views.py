from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import get_object_or_404,render_to_response,redirect
from apps.app.models import *
from django.http import HttpResponse,HttpResponseRedirect
from apps.app import iniciar_sesion, cerrar_sesion, menu, permiso_requerido
from datetime import datetime
# Create your views here.

#------------ Cliente ---------------
def clientes(request):	
	permiso_requerido(request)
	menuLista = menu(request)
	clientes = Cliente.objects.filter(estadoCliente="Activo")
	template = 'formVerClientes.html'
	return render(request, template, {'clientes': clientes, "listaMenu": menuLista})

def nuevo_cliente(request):
	menuLista = menu(request)
	lstProvincia = Provincia.objects.all()
	lstCiudad = Ciudad.objects.all()
	lstCiudad2 = Ciudad.objects.filter(provinciaCiudad = lstProvincia[0])
	lstPersona = Persona.objects.all().exclude(cedulaPersona = "0000000000")
	lstCliente = Cliente.objects.all()
	template = 'formRegistroClientes.html'
	return render(request, template, {"listaMenu": menuLista, 
			'lstProvincia': lstProvincia, 'lstCiudad': lstCiudad, 
			'lstCiudad2': lstCiudad2, 'lstCliente':lstCliente, 'lstPersona':lstPersona})

def editar_cliente(request, cliente_id):
	menuLista = menu(request)
	clienteSelec = Cliente.objects.get(id=cliente_id)	
	lstProvincia = Provincia.objects.all()
	lstCiudad = Ciudad.objects.all()
	idPro = clienteSelec.personaCliente.ciudadPersona.provinciaCiudad.id
	lstCiudad2 = Ciudad.objects.filter(provinciaCiudad = idPro)
	lstPersona = Persona.objects.all().exclude(cedulaPersona = "0000000000")
	template = 'formActualizarClientes.html'
	return render(request, template, {"listaMenu": menuLista, 'lstProvincia': lstProvincia, 
		'lstCiudad': lstCiudad, 'lstCiudad2': lstCiudad2, 'clienteSelec': clienteSelec,
		 'lstPersona':lstPersona})

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
		emp = Cliente()

		cedula = request.POST["cc_ruc"] 
		ciu = Ciudad(pk = request.POST['selectbasicC'])
		existeP = False; existeE = False
		if opcion == 0:
			try:
				per = Persona.objects.get(cedulaPersona=cedula)
				existeP = True
				emp = Cliente.objects.get(personaCliente=per)
				existeE = True;
			except:
				print("No hay persona o cliente")
		else:
			try:
				emp = Cliente.objects.get(pk=cliente_id)
				existeE = True;
				per = Persona.objects.get(pk=emp.personaCliente.id)
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

		emp.estadoCliente = estado
		emp.observacionesCliente = request.POST["observaciones"]
		emp.personaCliente = per
        emp.save()
        print("Elemento guardado!")
        return redirect('clientes')
	returnnse(template,context_instance=RequestContext(request, locals()))
#-------------------------------------


#------------ Factura ---------------
def facturas(request):
	menuLista = menu(request)
	lstFactura = Factura.objects.all().exclude(estadoFactura = "Anulado").order_by('-numeroFactura')
	template = 'formVerFacturas.html'
	return render(request, template, {"listaMenu": menuLista, "lstFactura": lstFactura})

def nuevo_factura(request):
	lstProducto = Producto.objects.all().exclude(cantidadProducto=0)
	lstCliente = Cliente.objects.all()
	lstFacturaNum = Factura.objects.values_list('numeroFactura', flat=True).all().exclude(estadoFactura="Anulado")
	dato = DatosEmpresa.objects.all()[0]
	template = 'formRegistroFacturas.html'
	return render(request, template, {"listaMenu": menu(request), "lstCliente":lstCliente,
		"lstProducto":lstProducto, 'dato':dato, 'lstFacturaNum': lstFacturaNum})

def enviar_factura(request, factura_id):
	response = ayuda_enviar_factura(request, factura_id)
	return response
	
def anular_factura(request, factura_id):
	facturaSelec = Factura.objects.get(id=factura_id)
	facturaSelec.estadoFactura = "Anulado"
	facturaSelec.save()
	return redirect('facturas')

def vista_factura(request, factura_id):
	facturaSelec = Factura.objects.get(pk=factura_id)
	lstDetalleFac = DetalleFactura.objects.filter(facturaDetalleFactura=facturaSelec)
	dato = DatosEmpresa.objects.all()[0]
	print(len(lstDetalleFac))
	template = 'formVistaFactura.html'
	return render(request, template, {"listaMenu": menu(request), 
		"facturaSelec":facturaSelec,"lstDetalleFac":lstDetalleFac,
		'dato':dato})

def guardar_factura(request):
	contador = request.GET['contador']
	print("contador: " + str(contador))
	numeroFac = request.GET['numeroFactura']
	print("numeroFactura"  +str(numeroFac))
	productoId = request.GET['productoId']
	print("productoId" + str(productoId))
	
	perAux = Persona.objects.get(cedulaPersona=request.GET['cliente'])
	fecha = datetime.strptime(request.GET['fecha'], "%d/%m/%Y").date()
	if str(contador)=="1":
		print("------------------>Contador CINCO" + str(perAux.id))
		clienteAux = Cliente.objects.get(personaCliente = perAux)
		datosempresa = DatosEmpresa.objects.all()
		print datosempresa
		facAux = Factura(
			numeroFactura=request.GET['numeroFactura'],
			fechaFactura=fecha,
			subtotalFactura=request.GET['subtotal'],
			descuentoFactura=request.GET['descuento'],
			ivaCeroFactura=request.GET['ivaCero'],
			ivaDoceFactura=request.GET['ivaDoce'],
			totalFactura=request.GET['total'],
			estadoFactura="Pendiente",
			observacionesFactura=request.GET['observaciones'],
			esCuentaCobrarFactura=request.GET['esCuenta'],
			datosEmpresaFactura=datosempresa[0],
			clienteFactura=clienteAux
			)
		facAux.save()
		print("--------------->factura guardada!")
		#try:
		#	facAux.save()
		#	print("asdadasdadsadsasadadsasd")
		#except Exception, e:
		#	print(e.message)
	facAux = Factura.objects.filter(numeroFactura = request.GET['numeroFactura']).exclude(estadoFactura="Anulado")
	print("---------> cantidad Factura: " + str(len(facAux)))
	print("Obtuvo factura")
	proAux = Producto.objects.get(id = productoId)
	detFac = DetalleFactura()
	detFac.cantidadDetalleFactura = request.GET['cantidad']
	detFac.precioDetalleFactura = request.GET['precio']
	detFac.facturaDetalleFactura = facAux[0]
	detFac.productoDetalleFactura = proAux
	detFac.save()
	print("Hola :D Detalle")
	obse = "(-) K Factura No. " + str(request.GET['numeroFactura'])
	print("Save kardex1")
	saldo = float(str(proAux.cantidadProducto)) - float(str(detFac.cantidadDetalleFactura))
	print("Save kardex2")
	kar = Kardex(
			fechaKardex=fecha,
			cantidadKardex=request.GET['cantidad'],
			precioUnitarioKardex=request.GET['totalPro'],
			saldoKardex=saldo,
			razonKardex= "MENOS",
			observacionesKardex=obse,
			personaKardex=perAux,
			productoKardex=proAux, 
			)
	kar.save();
	print("Save kardex")
	proAux.cantidadProducto = saldo
	proAux.save()
	print("Save producto")

#-------------------------------------


from io import BytesIO
from cStringIO import StringIO
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from apps.general import enviar_email_factura
from reportlab.lib.units import inch
def factura_pdf(request):
	pass
# Create your views here.
def ayuda_enviar_factura(request, idFac):
	pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
	pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
	pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
	pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))
	
	dato = DatosEmpresa.objects.all()[0]
	factura = Factura.objects.get(pk=idFac)
	detalle = DetalleFactura.objects.filter(facturaDetalleFactura=factura)
	deta = DetalleFactura.objects.filter(facturaDetalleFactura = factura)

	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=hello.pdf'
	buffer = BytesIO()
	# Create the PDF object, using the StringIO object as its "file."
	p = canvas.Canvas(buffer)
	p.setFont('Vera', 20)
	# Draw things on the PDF. Here's where the PDF generation happens.
	# See the ReportLab FIRST_DAY_OF_WEEK = 0cumentation for the full list of functionality.
	#------------------------Encabezado
	p.drawString(40,800,dato.nombreDatosEmpresa)
	p.setFont('Vera', 9)
	p.drawString(40,780,"-----------------------------------------------------------------------")
	p.drawString(40,770,"Venta al por mayor y menor de sabanas, toallas,")
	p.drawString(40,760,"cubrecamas y artefactos para el hogar.")
	p.drawString(40,750,"-----------------------------------------------------------------------")
	p.drawString(40,740,"Direc.:" + dato.direccionDatosEmpresa)
	p.drawString(40,730,"Tel.:" + dato.telefonoDatosEmpresa)

	p.drawString(350,800,"R.U.C. "+dato.nuestrosProductosDatosEmpresa)
	p.drawString(350,780,"FACTURA")
	p.drawString(350,770,"Serie 001-001-00")
	p.drawString(350,760,"      "+str(factura.numeroFactura))
	p.drawString(350,750,"--------------------------------------------")
	p.drawString(350,740,"AUT. SRI.: 1114411008")
	p.drawString(350,730,"Fecha: " + str(factura.fechaFactura))
	#######################################
	p.drawString(40,700, "Cliente: "+ factura.clienteFactura.personaCliente.apellidosPersona + " " + factura.clienteFactura.personaCliente.nombresPersona)
	p.drawString(40,690, "Direccion: " + factura.clienteFactura.personaCliente.direccionPersona)
	p.drawString(40,680, "R.U.C/CI: " + factura.clienteFactura.personaCliente.cedulaPersona)
	p.setFillColorRGB(0,0.77,0.99)
	p.rect(40,640,510,30,stroke=1, fill = 1)
	p.setFillColorRGB(0,0,0)
	##DETALLE
	p.drawString(45,650,"CODIGO")
	p.drawString(100,650,"DESCRIPCION")
	p.drawString(350,650,"CANTIDAD")
	p.drawString(420,650,"PRECIO UN.")
	p.drawString(500,650,"TOTAL")
	#p.line(40,660,540,660)#horizontal
	#p.line(40,630,540,660)#horizontal
	#p.line(40,50,40,660)#vertical
	posicion = 620
	for det in detalle:
		p.setFillColorRGB(1,1,1)
		p.rect(40,posicion-10,510,30,stroke=1, fill = 1)
		p.setFillColorRGB(0,0,0)
		p.drawString(45,posicion,det.productoDetalleFactura.codigoProducto)
		p.drawString(100,posicion,det.productoDetalleFactura.descripcionProducto)
		p.drawString(350,posicion,str(det.cantidadDetalleFactura))
		p.drawString(420,posicion,str(det.precioDetalleFactura))
		total = round(det.cantidadDetalleFactura *det.precioDetalleFactura,2) 
		p.drawString(500,posicion,str(total))
		posicion = posicion - 29
	posicion = posicion + 6	
	p.setFillColorRGB(1,1,1)
	p.rect(340,posicion-4,210,15,stroke=1, fill = 1)
	p.setFillColorRGB(0,0,0)
	p.drawString(350,posicion,"SUBTOTAL:")
	p.drawRightString(530,posicion,str(factura.subtotalFactura))
	posicion = posicion - 15
	p.setFillColorRGB(1,1,1)
	p.rect(340,posicion-4,210,15,stroke=1, fill = 1)
	p.setFillColorRGB(0,0,0)
	p.drawString(350,posicion,"DESCUENTO (-):")
	p.drawRightString(530,posicion,str(factura.descuentoFactura))
	posicion = posicion - 15
	p.setFillColorRGB(1,1,1)
	p.rect(340,posicion-4,210,15,stroke=1, fill = 1)
	p.setFillColorRGB(0,0,0)
	p.drawString(350,posicion,"IVA 12% (+):")
	p.drawRightString(530,posicion,str(factura.ivaDoceFactura))	
	posicion = posicion - 15
	p.setFillColorRGB(1,1,1)
	p.rect(340,posicion-4,210,15, stroke=1, fill = 1)
	p.setFillColorRGB(0,0,0)
	p.drawString(350,posicion,"TOTAL: ")
	p.drawRightString(530,posicion,str(factura.totalFactura))	
	#p.setFillColorRGB(0,0,0)
	#p.drawString(350,posicion,"TOTAL: " + str(factura.totalFactura))

	p.showPage()
	p.save()
	# Get the value of the BytesIO buffer and write it to the response.
	pdf = buffer.getvalue()
	buffer.close()
	try:
		print("Ok11111")
		emisor = str(dato.emailDatosEmpresa)
		print("Ok111")
		clave = str(dato.claveDatosEmpresa)
		print("Ok11")
		asunto = str(dato.nombreDatosEmpresa) + " - FACTURA"
		print("Ok1")
		receptor = str(factura.clienteFactura.personaCliente.emailPersona)
		print("Ok2")
		nombreDoc = "FAC - " + str(factura.numeroFactura) 
		print("Ok3")
		enviar_email_factura(emisor, clave, asunto, receptor, pdf, nombreDoc)
		#
		#enviar_email_factura(dato.emailDatosEmpresa, dato.claveDatosEmpresa,
		# "Creditos Vacacela - Factura","estefaniavacacela@gmail.com", pdf)
		#enviar_email_factura("estefaniavacacela@gmail.com", "JamasDireNunca", 
		#user, password, asunto, destinatario, pdf
		#	"Factura 001-Creditos Vacacela", "akirevacacela@gmail.com")
	except:
		print ("Mal")
	response.write(pdf)
	return response
