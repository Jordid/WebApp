from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import get_object_or_404,render_to_response,redirect
from apps.app.models import Categoria, Producto, Kardex, Persona
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from apps.app import iniciar_sesion, cerrar_sesion, menu, login_requerido
from datetime import datetime
# Create your views here.


#------------ Categoria ---------------
def categorias(request):
	lstCategoria = Categoria.objects.all()
	template = 'formVerCategorias.html'
	return render(request, template, {"listaMenu": menu(request), "lstCategoria": lstCategoria})

def nuevo_categoria(request):
	categoriaSelec = Categoria(id=0)
	lstCategoria = Categoria.objects.all()
	template = 'formRegistroCategorias.html'
	return render(request, template, {"listaMenu": menu(request), 'categoriaSelec': categoriaSelec,
		'lstCategoria':lstCategoria})

def editar_categoria(request, categoria_id):
	categoriaSelec = Categoria.objects.get(id=categoria_id)	
	template = 'formRegistroCategorias.html'
	return render(request, template, {"listaMenu": menu(request), 'categoriaSelec': categoriaSelec})

def eliminar_categoria(request, categoria_id):
	categoriaSelec = Categoria.objects.get(id=categoria_id)
	categoriaSelec.estadoEmpleado = "Inactivo"
	categoriaSelec.save()
	return redirect('categorias')

def guardar_categoria(request, categoria_id):
	template = ""
	opcion = int(str(categoria_id))
	if opcion == 0:
		template = "formRegistroCategorias.html"
	else:
		template = "formActualizarCategorias.html"

	if request.POST:
		cat = Categoria()
		if opcion != 0:
			cat= Categoria.objects.get(id = categoria_id)
		
		cat.descripcionCategoria = request.POST["descripcion"]
		cat.save()
        return redirect('categorias')
	returnnse(template,context_instance=RequestContext(request, locals()))
#-------------------------------------

#------------ Producto ---------------
def productos(request):
	lstProducto = Producto.objects.all()
	template = 'formVerProductos.html'
	return render(request, template, {"listaMenu": menu(request), "lstProducto": lstProducto})

def nuevo_producto(request):
	lstCategoria = Categoria.objects.all()
	template = 'formRegistroProductos.html'
	return render(request, template, {"listaMenu": menu(request), 'lstCategoria': lstCategoria})

def editar_producto(request, producto_id):
	productoSelec = Producto.objects.get(id=producto_id)	
	lstCategoria = Categoria.objects.all()
	template = 'formActualizarProductos.html'
	return render(request, template, {"listaMenu": menu(request), 'lstCategoria': lstCategoria, 
		'productoSelec': productoSelec})

def eliminar_producto(request, producto_id):
	productoSelec = Producto.objects.get(id=producto_id)
	productoSelec.estadoProducto = "Inactivo"
	productoSelec.save()
	return redirect('productos')

def guardar_producto(request, producto_id):
	template = ""
	opcion = int(str(producto_id))
	if opcion == 0:
		template = "formRegistroProductos.html"
	else:
		template = "formActualizarProductos.html"

	if request.POST:
		cat = Categoria()
		pro = Producto()
		estado = "Activo"
		if opcion != 0:
			estado = request.POST["estado"]
			pro= Producto.objects.get(id = producto_id)		
		cat.id = request.POST["selectbasic"]
		pro.codigoProducto = request.POST["codigo"]
		pro.descripcionProducto = request.POST["descripcion"]
		if opcion == 0:
			pro.cantidadProducto = 0
		
		pro.stockMinimoProducto =request.POST ["stockMinimo"]
		pro.costoProducto =request.POST["costo"]
		pro.valorAgregadoProducto =request.POST["valorAgregado"]
		pro.ivaProducto =request.POST["iva"]
		pro.precioContadoProducto =request.POST["precioContado"]
		pro.precioCreditoProducto =request.POST["precioCredito"]
		pro.marcaProducto =request.POST["marca"]
		pro.estadoProducto = estado
		pro.categoriaProducto = cat
		pro.save()
        return redirect('productos')
	returnnse(template,context_instance=RequestContext(request, locals()))

#-------------------------------------


#------------ Kardex ---------------
def ingreso_kardex(request):
	lstPersona = Persona.objects.all()
	lstProducto = Producto.objects.all()#.exclude(cantidadProducto=0)
	lstKardex = Kardex.objects.all()
	razon="MAS"
	template = 'formRegistroKardex.html'
	return render(request, template, {"listaMenu": menu(request), "lstKardex": lstKardex,
		'lstPersona':lstPersona, 'lstProducto':lstProducto, 'razon':razon})

def salida_kardex(request):
	lstPersona = Persona.objects.all()
	lstProducto = Producto.objects.all().exclude(cantidadProducto=0)
	lstKardex = Kardex.objects.all()
	razon="MENOS"
	template = 'formRegistroKardex.html'
	return render(request, template, {"listaMenu": menu(request), "lstKardex": lstKardex,
		'lstPersona':lstPersona, 'lstProducto':lstProducto, 'razon':razon})

def kardex(request):
	lstKardex = Kardex.objects.all()
	lstProducto = Producto.objects.all()
	template = 'formVerKardex.html'
	return render(request, template, {"listaMenu": menu(request), 
		"lstKardex": lstKardex, 'lstProducto':lstProducto})

def guardar_kardex(request):
	template = "formRegistroKardex.html"
	if request.POST:
		fecha = datetime.strptime(request.POST['fecha'], "%d/%m/%Y").date()
		per = Persona.objects.get(cedulaPersona=request.POST['cc_ruc'])
		pro = Producto.objects.get(pk=request.POST['country'])
		obse =""
		if str(request.POST['razon'])=="MAS":
			obse = obse + "(+) K "
		else:
			obse = obse + "(-) K "
		obse=obse+request.POST['fecha']
		kar = Kardex(
			fechaKardex=fecha,
			cantidadKardex=request.POST['cantidad'],
			precioUnitarioKardex=request.POST['precio'],
			saldoKardex=request.POST['saldo'],
			razonKardex=request.POST['razon'],
			observacionesKardex=obse,
			personaKardex=per,
			productoKardex=pro, 
			)
		kar.save();
		pro.cantidadProducto = request.POST['saldo']
		pro.save()
		print("Ok");
        return redirect('kardex')
	returnnse(template,context_instance=RequestContext(request, locals()))
#-------------------------------------
