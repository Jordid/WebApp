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
	lstCuentaNum = CuentaCobrar.objects.values_list('numeroCuentaCobrar', flat=True).all().exclude(estadoCuentaCobrar="Anulado")
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
	contador = request.GET['contador']
	print("contador: " + str(contador))
	numeroCuenta = request.GET['numeroCuenta']
	print("numeroCuenta"  +str(numeroCuenta))

	if str(contador)=="1":
		clienteAux = Cliente.objects.get(pk=request.GET['idClienteAux'])
		print("ENTRO....................................3")
		ciudadAux = Ciudad.objects.get(pk=request.GET['ciudadID'] )
		print("ENTRO....................................6")
		fecha=datetime.strptime(request.GET['fechaAc'], "%d/%m/%Y").date()
		fechaA=datetime.strptime(request.GET['fechaCIn'], "%d/%m/%Y").date()
		print("ENTRO....................................7")
		cuenAux = CuentaCobrar(
			numeroCuentaCobrar=request.GET['numeroCuenta'],
			fechaCuetaCobrar=fecha,
			fechaInicioPagoCuentaCobrar=fechaA,
			cuotaInicialCuentaCobrar=request.GET['cuotaInicial'],
			cuotaCuentaCobrar=request.GET['cuotas'],
			formaPagoCuentaCobrar =request.GET['formaPago'],
			totalCuentaCobrar=request.GET['total'],
			saldoCuentaCobrar=request.GET['saldo'],
			observacionesCuentaCobrar=request.GET['observaciones'],
			estadoCuentaCobrar="Pendiente",
			ciudadCuentaCobrar=ciudadAux,
			clienteCuentaCobrar=clienteAux
			)
		cuenAux.save()
		print("Guarde cuenta!")
	print("Hola :D 2")
	cuentaA = CuentaCobrar.objects.filter(numeroCuentaCobrar=request.GET['numeroCuenta']).exclude(estadoCuentaCobrar="Anulado")
	print("Cantidad de mi cuenta ="+ str(len(cuenAux.count())))
	productoA = Producto.objects.get(id = request.GET['productoId'])
	detCuenta = DetalleCuentaCobrar(
		cantidadDetCueCob=request.GET['cantidad'],
		precioDetCueCob=request.GET['precio'],
		cuentaCobrarDetCueCob=cuentaA[0],
		productoDetCueCob=productoA
		)
	detCuenta.save()
	print("Hola :D detalle")
	

def guardar_detalle_cuenta_por_cobrar(request):
	pass

def insertar_abono_cuenta_por_cobrar(request):
	print("OK")
	cuentaNumero = request.GET['numeroCuenta'] 
	print("OK2")
	fecha=datetime.strptime(request.GET['fecha'], "%d/%m/%Y").date()
	cuentaAux = CuentaCobrar.objects.get(numeroCuentaCobrar=cuentaNumero)
	aboAux = AbonoCuentaCobrar()
	aboAux.cuentaCobrarAbonoCuentaCobrar = cuentaAux
	aboAux.numeroReciboAbonoCuentaCobrar = request.GET['numeroRecibo']
	aboAux.fechaAbonoCuentaCobrar = fecha
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