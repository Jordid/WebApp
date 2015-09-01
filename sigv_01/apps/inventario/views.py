from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import get_object_or_404,render_to_response,redirect
from apps.app.models import Categoria, Producto, Kardex
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from apps.app import iniciar_sesion, cerrar_sesion, menu, login_requerido
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
def kardex(request):
	lstKardex = Kardex.objects.all()
	template = 'formVerKardex.html'
	return render(request, template, {"listaMenu": menu(request), "lstKardex": lstKardex})
#-------------------------------------
