from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import get_object_or_404,render_to_response,redirect
from apps.app.models import *
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from apps.app import menu
from decimal import Decimal
# Create your views here.

#------------ CuentaCobrar ---------------
def cuentas_por_cobrar(request):
	lstCuentaCobrar = CuentaCobrar.objects.all()
	template = 'formVerCuentasPorCobrar.html'
	return render(request, template, {"listaMenu": menu(request), "lstCuentaCobrar": lstCuentaCobrar})

def nuevo_cuenta_por_cobrar(request):
	lstProducto = Producto.objects.all()
	lstCliente = Cliente.objects.all();
	lstProvincia = Provincia.objects.all()
	lstCiudad = Ciudad.objects.all()
	lstCiudad2 = Ciudad.objects.filter(provinciaCiudad = lstProvincia[0])
	template = 'formRegistroCuentasPorCobrar.html'
	return render(request, template, {"listaMenu": menu(request),"lstCliente":lstCliente,
		"lstProducto":lstProducto, 'lstProvincia': lstProvincia, 'lstCiudad': lstCiudad, 'lstCiudad2': lstCiudad2})

def vista_cuenta_por_cobrar(request, cuenta_id):
	cuentaSelec = CuentaCobrar.objects.get(pk=cuenta_id)
	lstDetalleCue = DetalleCuentaCobrar.objects.filter(cuentaCobrarDetCueCob=cuentaSelec)
	lstProvincia = Provincia.objects.all()
	lstCiudad = Ciudad.objects.all()
	idPro = cuentaSelec.ciudadCuentaCobrar.provinciaCiudad.id
	lstCiudad2 = Ciudad.objects.filter(provinciaCiudad = idPro)
	template = 'formVistaCuentaPorCobrar.html'
	return render(request, template, {"listaMenu": menu(request), "cuentaSelec":cuentaSelec,
		"lstDetalleCue":lstDetalleCue, 'lstProvincia': lstProvincia, 'lstCiudad': lstCiudad, 'lstCiudad2': lstCiudad2})

def abonar_cuenta_por_cobrar(request, cuenta_id):
	cuentaSelec = CuentaCobrar.objects.get(pk=cuenta_id)
	lstAbonos = AbonoCuentaCobrar.objects.filter(cuentaCobrarAbonoCuentaCobrar=cuentaSelec)
	ciudadSelec = Ciudad.objects.get(pk = cuentaSelec.ciudadCuentaCobrar.id)
	provinciaSelec = Provincia.objects.get(pk = ciudadSelec.provinciaCiudad.id)
	lugar = provinciaSelec.nombreProvincia + " - " + ciudadSelec.nombreCiudad
	template = 'formRegistroAbonosCuentasPorCobrar.html'
	return render(request, template, {"listaMenu": menu(request), "cuentaSelec":cuentaSelec,
		"lstAbonos":lstAbonos, 'lugar': lugar})

def guardar_cuenta_por_cobrar(request):
	clienteCed = request.GET['cliente'] 
	perAux = Persona.objects.get(cedulaPersona=clienteCed)
	clienteAux = Cliente.objects.get(personaCliente = perAux)
	ciudadAux = Ciudad.objects.get(pk=request.GET['ciudadID'] )

	cueAux = CuentaCobrar()
	cueAux.numeroCuentaCobrar = request.GET['numeroCuenta']
	print("Ok")
	print(request.GET['fechaAc'])
	fecha = datetime.strptime(request.GET['fechaAc'], "%d/%m/%Y").date()
	print(type(fecha))
	print("Fecha")
	cueAux.fechaCuetaCobrar =  fecha
	
	print(request.GET['fechaAc'])
	cueAux.fechaInicioPagoCuentaCobrar = datetime.strptime(request.GET['fechaCIn'], "%d/%m/%Y").date()
	print(":(())")
	print(cueAux.fechaInicioPagoCuentaCobrar)
	print(type(cueAux.fechaInicioPagoCuentaCobrar))
	cueAux.cuotaInicialCuentaCobrar = request.GET['cuotaInicial']
	cueAux.cuotaCuentaCobrar = request.GET['cuotas']
	cueAux.formaPagoCuentaCobrar = request.GET['formaPago']
	cueAux.totalCuentaCobrar = request.GET['total']
	cueAux.saldoCuentaCobrar = request.GET['saldo']
	cueAux.estadoCuentaCobrar = "PENDIENTE"
	cueAux.ciudadCuentaCobrar = ciudadAux
	cueAux.clienteCuentaCobrar = clienteAux
	cueAux.observacionesCuentaCobrar = request.GET['observaciones']
	cueAux.save()

	print("Ok cuenta")

def guardar_detalle_cuenta_por_cobrar(request):
	numeroCue = request.GET['numeroCuenta'] 
	print("Hola :D 1")
	productoId = request.GET['productoId']
	print("Hola :D 2")
	cuenta = CuentaCobrar.objects.get(numeroCuentaCobrar = numeroCue)
	producto = Producto.objects.get(id = productoId)
	print("Hola :D 3")
	detCuenta = DetalleCuentaCobrar()
	detCuenta.cantidadDetCueCob = request.GET['cantidad']
	print("Hola :D 4")
	detCuenta.precioDetCueCob = request.GET['precio']
	print("Hola :D 5")
	detCuenta.cuentaCobrarDetCueCob = cuenta
	detCuenta.productoDetCueCob = producto
	detCuenta.save()
	print("Hola :D detalle")

def insertar_abono_cuenta_por_cobrar(request):
	cuentaNumero = request.GET['numeroCuenta'] 
	cuentaAux = CuentaCobrar.objects.get(numeroCuentaCobrar=cuentaNumero)
	aboAux = AbonoCuentaCobrar()
	aboAux.cuentaCobrarAbonoCuentaCobrar = cuentaAux
	aboAux.numeroReciboAbonoCuentaCobrar = request.GET['numeroRecibo']
	aboAux.fechaAbonoCuentaCobrar = request.GET['fecha']
	aboAux.montoAbonoCuentaCobrar = request.GET['monto']
	aboAux.saldoAbonoCuentaCobrar = request.GET['saldo']
	aboAux.save()
	cuentaAux.saldoCuentaCobrar = request.GET['saldo']
	cuentaAux.save()
	print("Ok Abono")

def eliminar_abono_cuenta_por_cobrar(request):
	cuentaNumero = request.GET['numeroCuenta'] 
	cuentaAux = CuentaCobrar.objects.get(numeroCuentaCobrar=cuentaNumero)
	montoAbono = str(request.GET['monto'])
	montoAbono= Decimal(montoAbono.replace(",", "."))
	saldoNuevo = cuentaAux.saldoCuentaCobrar + montoAbono
	cuentaAux.saldoCuentaCobrar = saldoNuevo
	cuentaAux.save()

	AbonoCuentaCobrar.objects.get(pk = request.GET['idAbono']).delete()
	print("Ok Abono Eliminado")

#-------------------------------------


#------------ CuentaPagar ---------------
def cuentas_por_pagar(request):
	lstCuentaPagar = CuentaPagar.objects.all()
	template = 'formVerCuentasPorPagar.html'
	return render(request, template, {"listaMenu": menu(request), "lstCuentaPagar": lstCuentaPagar})
#-------------------------------------