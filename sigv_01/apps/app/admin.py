from django.contrib import admin
from models import *

class ProvinciaAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombreProvincia')

class CiudadAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombreCiudad', 'provinciaCiudad')
	list_filter = ('provinciaCiudad', )
	search_fields = ('nombreCiudad',)

class PersonaAdmin(admin.ModelAdmin):
	list_display = ('id', 'cedulaPersona', 'apellidosPersona', 'nombresPersona', 'telefonoPersona', 'direccionPersona', 'emailPersona', 'ciudadPersona')
	raw_id_fields = ('ciudadPersona',)
	search_fields = ('cedulaPersona',)
	#list_editable = ('cedulaPersona', 'apellidosPersona') campos editables
	#inlines 

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('id', 'estadoCliente', 'personaCliente')
	list_filter = ('estadoCliente', )

class EmpleadoAdmin(admin.ModelAdmin):
	list_display = ('id', 'cargoEmpleado', 'observacionesEmpleado','estadoEmpleado', 'personaEmpleado')
	list_filter = ('cargoEmpleado', )
	search_fields = ('cargoEmpleado',)

class ProveedorAdmin(admin.ModelAdmin):
	list_display = ('id', 'estadoProveedor', 'personaProveedor')
	list_filter = ('estadoProveedor', )

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('id', 'descripcionCategoria')

class ProductoAdmin(admin.ModelAdmin):
	list_display = ('id', 'codigoProducto', 'descripcionProducto', 'cantidadProducto',
	'stockMinimoProducto',  'costoProducto', 'valorAgregadoProducto','ivaProducto',
	'precioContadoProducto', 'precioCreditoProducto', 'marcaProducto', 'estadoProducto',
	'categoriaProducto')
	list_filter = ('categoriaProducto', )

class KardexAdmin(admin.ModelAdmin):
	list_display = ('id', 'fechaKardex', 'cantidadKardex', 'precioUnitarioKardex',
	'saldoKardex','razonKardex','observacionesKardex','personaKardex','productoKardex' )
	list_filter = ('razonKardex', )

class AvisoAdmin(admin.ModelAdmin):
	list_display = ('id', 'tipoAviso', 'descripcionAviso')

class CuentaCobrarAdmin(admin.ModelAdmin):
	list_display = ('id', 'numeroCuentaCobrar', 'fechaCuetaCobrar', 'fechaInicioPagoCuentaCobrar',
		'cuotaInicialCuentaCobrar','cuotaCuentaCobrar','formaPagoCuentaCobrar',
		'totalCuentaCobrar','saldoCuentaCobrar','observacionesCuentaCobrar',
		'estadoCuentaCobrar', 'ciudadCuentaCobrar', 'clienteCuentaCobrar' )

class NotificacionAdmin(admin.ModelAdmin):
	list_display = ('id', 'fechaNotificacion', 'observacionesNotificacion',
		'cuentaCobrar', 'aviso')

class DetalleCuentaCobrarAdmin(admin.ModelAdmin):
	list_display = ('id', 'cantidadDetCueCob', 'precioDetCueCob',
		'cuentaCobrarDetCueCob', 'productoDetCueCob')

class AbonoCuentaCobrarAdmin(admin.ModelAdmin):
	list_display = ('id', 'fechaAbonoCuentaCobrar', 'montoAbonoCuentaCobrar',
		'saldoAbonoCuentaCobrar', 'numeroReciboAbonoCuentaCobrar', 'cuentaCobrarAbonoCuentaCobrar')
		
class CuentaPagarAdmin(admin.ModelAdmin):
	list_display = ('id', 'numeroCuentaPagar', 'fechaCuentaPagar', 'cuotaInicialCuentaPagar',
		'cuotasCuentaPagar','totalCuentaPagar','saldoCuentaPagar',
		'observacionesCuentaPagar','estadoCuentaPagar','personaCuentaPagar',)

class AbonoCuentaPagarAdmin(admin.ModelAdmin):
	list_display = ('id', 'fechaAbonoCuentaPagar', 'montoAbonoCuentaPagar',
		'saldoAbonoCuentaPagar', 'observacionesAbonoCuentaPagar', 'cuentaPagarAbonoCuentaPagar')

class DatosEmpresaAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombreDatosEmpresa', 'direccionDatosEmpresa',
		'telefonoDatosEmpresa', 'misionDatosEmpresa', 'visionDatosEmpresa',
		'nuestrosProductosDatosEmpresa','quienesSomosDatosEmpresa', 'logoDatosEmpresa',
		'emailDatosEmpresa')

class FacturaAdmin(admin.ModelAdmin):
	list_display = ('id', 'numeroFactura', 'fechaFactura', 'subtotalFactura',
		'descuentoFactura', 'ivaCeroFactura', 'ivaDoceFactura', 'totalFactura',
		'estadoFactura','datosEmpresaFactura', 'clienteFactura')

class DetalleFacturaAdmin(admin.ModelAdmin):
	list_display = ('id', 'cantidadDetalleFactura', 'precioDetalleFactura', 
		'facturaDetalleFactura', 'productoDetalleFactura')

class UsuarioAdmin(admin.ModelAdmin):
	list_display = ('id', 'nickUsuario', 'claveUsuario', 'estadoUsuario','personaUsuario',)

class RolAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombreRol',)

class UsuarioRolesAdmin(admin.ModelAdmin):
	list_display = ('id', 'rolUsuarioRoles', 'usuarioUsuarioRoles', )

class MenuAdmin(admin.ModelAdmin):
	list_display = ('id', 'codigoMenu', 'descripcionMenu', 'posicionMenu' ,
		'iconoMenu', 'estadoMenu', 'urlMenu', 'codigoPadreMenu')
	list_editable = ('posicionMenu', 'estadoMenu','urlMenu', )

class PermisosAdmin(admin.ModelAdmin):
	list_display = ('id', 'rolPermiso', 'menuPermiso',)


# Register your models here.
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Kardex, KardexAdmin)
admin.site.register(Aviso, AvisoAdmin)
admin.site.register(CuentaCobrar, CuentaCobrarAdmin)
admin.site.register(AbonoCuentaCobrar, AbonoCuentaCobrarAdmin)
admin.site.register(Notificacion, NotificacionAdmin)
admin.site.register(DetalleCuentaCobrar, DetalleCuentaCobrarAdmin)
admin.site.register(CuentaPagar, CuentaPagarAdmin)
admin.site.register(AbonoCuentaPagar, AbonoCuentaPagarAdmin)
admin.site.register(DatosEmpresa, DatosEmpresaAdmin)
admin.site.register(Factura, FacturaAdmin)
admin.site.register(DetalleFactura, DetalleFacturaAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Rol, RolAdmin)
admin.site.register(UsuarioRoles, UsuarioRolesAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Permisos, PermisosAdmin)
