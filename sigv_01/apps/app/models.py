from django.db import models

# Create your models here.
class Provincia(models.Model):
	nombreProvincia = models.CharField(max_length = 100)

	def __unicode__(self):
		return '%s'%(self.nombreProvincia)

class Ciudad(models.Model):
	nombreCiudad = models.CharField(max_length = 100)
	provinciaCiudad = models.ForeignKey(Provincia)

	def __unicode__(self):
		return '%s'%(self.nombreCiudad)

class Persona(models.Model):
	cedulaPersona = models.CharField(max_length = 20)
	apellidosPersona = models.CharField(max_length = 50)
	nombresPersona = models.CharField(max_length = 50)
	telefonoPersona = models.CharField(max_length = 10)
	direccionPersona = models.TextField(help_text = 'Redacte la direccion')
	emailPersona = models.EmailField(max_length = 50)
	ciudadPersona = models.ForeignKey(Ciudad)

	def __unicode__(self):
		return '%s - %s'%(self.cedulaPersona, self.apellidosPersona + " "+ self.nombresPersona)

class Empleado(models.Model):
	cargoEmpleado = models.CharField(max_length = 50)
	observacionesEmpledo = models.TextField(default="", help_text = 'Redacte las observaciones')
	estadoEmpleado = models.CharField(max_length=20)
	personaEmpleado = models.ForeignKey(Persona)

class Proveedor(models.Model):
	estadoProveedor = models.CharField(max_length = 20)
	personaProveedor = models.ForeignKey(Persona)

class Cliente(models.Model):
	estadoCliente = models.CharField(max_length = 20)
	observacionesCliente = models.TextField(default="")
	personaCliente = models.ForeignKey(Persona)

class Usuario(models.Model):
	nickUsuario = models.CharField(max_length=20)
	claveUsuario = models.TextField(default="")
	estadoUsuario = models.CharField(max_length=20)
	personaUsuario = models.ForeignKey(Persona)	

#-------Seccion Bodega-------#
class Categoria(models.Model):
	descripcionCategoria = models.CharField(max_length = 100)

	def __unicode__(self):
		return '%s'%(self.descripcionCategoria)

class Producto(models.Model):
	codigoProducto = models.CharField(max_length = 20)
	descripcionProducto = models.TextField()
	cantidadProducto = models.DecimalField(max_digits = 20,decimal_places = 2)
	stockMinimoProducto = models.DecimalField(max_digits = 20,decimal_places = 2)
	costoProducto = models.DecimalField(max_digits = 20,decimal_places = 2)
	valorAgregadoProducto = models.DecimalField(max_digits = 20,decimal_places = 2)
	ivaProducto = models.DecimalField(max_digits = 20,decimal_places = 2)
	precioContadoProducto = models.DecimalField(max_digits = 20,decimal_places = 2)
	precioCreditoProducto = models.DecimalField(max_digits = 20,decimal_places = 2)
	marcaProducto = models.TextField(default="")
	estadoProducto = models.CharField(max_length = 20)
	categoriaProducto = models.ForeignKey(Categoria)


class Kardex(models.Model):
	fechaKardex = models.DateTimeField(auto_now=True)
	cantidadKardex = models.DecimalField(max_digits = 20,decimal_places = 2)
	precioUnitarioKardex = models.DecimalField(max_digits = 20,decimal_places = 2)
	saldoKardex = models.DecimalField(max_digits = 20,decimal_places = 2)
	razonKardex = models.CharField(max_length = 5)
	observacionesKardex = models.TextField(default="")
	personaKardex = models.ForeignKey(Persona)
	productoKardex = models.ForeignKey(Producto)

class Aviso(models.Model):
	tipoAviso = models.CharField(max_length=50)
	descripcionAviso = models.TextField(default="", help_text = 'Redacte las observaciones')

class CuentaCobrar(models.Model):
	numeroCuentaCobrar = models.IntegerField(default = 0)
	fechaCuetaCobrar = models.DateField(auto_now = True)
	fechaInicioPagoCuentaCobrar = models.DateField(auto_now = True)
	cuotaInicialCuentaCobrar = models.DecimalField(max_digits = 20,decimal_places = 2)
	cuotaCuentaCobrar = models.DecimalField(max_digits = 20,decimal_places = 2)
	formaPagoCuentaCobrar = models.CharField(max_length=10)
	totalCuentaCobrar = models.DecimalField(max_digits = 20,decimal_places = 2)
	saldoCuentaCobrar = models.DecimalField(max_digits = 20,decimal_places = 2)
	observacionesCuentaCobrar = models.TextField(default="")
	estadoCuentaCobrar = models.CharField(max_length=20)
	ciudadCuentaCobrar = models.ForeignKey(Ciudad)
	clienteCuentaCobrar = models.ForeignKey(Cliente)

class Notificacion(models.Model):
	fechaNotificacion = models.DateField(auto_now=True)
	observacionesNotificacion = models.TextField(default="", help_text = 'Redacte las observaciones')
	cuentaCobrar = models.ForeignKey(CuentaCobrar)
	aviso = models.ForeignKey(Aviso)

class DetalleCuentaCobrar(models.Model):
	cantidadDetCueCob = models.DecimalField(max_digits = 20,decimal_places = 2)
	precioDetCueCob = models.DecimalField(max_digits = 20,decimal_places = 2) 
	cuentaCobrarDetCueCob = models.ForeignKey(CuentaCobrar)
	productoDetCueCob = models.ForeignKey(Producto)

class AbonoCuentaCobrar(models.Model):
	fechaAbonoCuentaCobrar = models.DateField(auto_now=True)
	montoAbonoCuentaCobrar = models.DecimalField(max_digits = 20,decimal_places = 2)
	saldoAbonoCuentaCobrar = models.DecimalField(max_digits = 20,decimal_places = 2)
	numeroReciboAbonoCuentaCobrar = models.IntegerField(default = 0)
	cuentaCobrarAbonoCuentaCobrar = models.ForeignKey(CuentaCobrar)

class CuentaPagar(models.Model):
	numeroCuentaPagar = models.IntegerField(default=0)
	fechaCuentaPagar = models.DateField(auto_now=True)
	cuotaInicialCuentaPagar = models.DecimalField(max_digits = 20,decimal_places = 2)
	cuotasCuentaPagar = models.DecimalField(max_digits = 20,decimal_places = 2)
	totalCuentaPagar = models.DecimalField(max_digits = 20,decimal_places = 2)
	saldoCuentaPagar = models.DecimalField(max_digits = 20,decimal_places = 2)
	observacionesCuentaPagar = models.TextField(default="", help_text = 'Redacte las observaciones')
	estadoCuentaPagar = models.CharField(max_length=20)
	personaCuentaPagar = models.ForeignKey(Proveedor)

class AbonoCuentaPagar(models.Model):
	fechaAbonoCuentaPagar = models.DateField(auto_now = True)
	montoAbonoCuentaPagar = models.DecimalField(max_digits = 20,decimal_places = 2)
	saldoAbonoCuentaPagar = models.DecimalField(max_digits = 20,decimal_places = 2)
	observacionesAbonoCuentaPagar = models.TextField(default="", help_text = 'Redacte las observaciones')
	cuentaPagarAbonoCuentaPagar = models.ForeignKey(CuentaPagar)

class DatosEmpresa(models.Model):
	nombreDatosEmpresa = models.CharField(max_length= 50)
	direccionDatosEmpresa = models.CharField(max_length= 100)
	telefonoDatosEmpresa = models.CharField(max_length= 21)
	misionDatosEmpresa = models.TextField(default="")
	visionDatosEmpresa = models.TextField(default="")
	nuestrosProductosDatosEmpresa = models.TextField(default="")
	quienesSomosDatosEmpresa = models.TextField(default="")
	logoDatosEmpresa = models.URLField(default="")
	emailDatosEmpresa = models.EmailField(max_length=50)
	#ciudadDatosEmpresa = models.ForeignKey(Ciudad)

class Factura(models.Model):
	numeroFactura = models.IntegerField(default=0)
	fechaFactura = models.DateField(auto_now = True)
	subtotalFactura = models.DecimalField(max_digits = 20,decimal_places = 2)
	descuentoFactura = models.DecimalField(max_digits = 20,decimal_places = 2)
	ivaCeroFactura = models.DecimalField(max_digits = 20,decimal_places = 2)
	ivaDoceFactura = models.DecimalField(max_digits = 20,decimal_places = 2)
	totalFactura = models.DecimalField(max_digits = 20,decimal_places = 2)
	estadoFactura = models.CharField(max_length=20)
	observacionesFactura = models.TextField(default="")
	datosEmpresaFactura = models.ForeignKey(DatosEmpresa)
	clienteFactura = models.ForeignKey(Cliente)

class DetalleFactura(models.Model):
	cantidadDetalleFactura = models.DecimalField(max_digits = 20,decimal_places = 2)
	precioDetalleFactura = models.DecimalField(max_digits = 20,decimal_places = 2)
	facturaDetalleFactura = models.ForeignKey(Factura)
	productoDetalleFactura = models.ForeignKey(Producto)

class Rol(models.Model):
	nombreRol = models.CharField(max_length=30)

	def __unicode__(self):
		return '%s'%(self.nombreRol)

class UsuarioRoles(models.Model):
	rolUsuarioRoles = models.ForeignKey(Rol)
	usuarioUsurioRoles = models.ForeignKey(Usuario)

class Menu(models.Model):
	codigoMenu = models.CharField(max_length=20)
	descripcionMenu = models.TextField(default="")
	posicionMenu = models.IntegerField(default=0)
	iconoMenu = models.URLField()
	estadoMenu = models.CharField(max_length=20)
	urlMenu = models.TextField(default="")
	codigoPadreMenu = models.CharField(max_length=20)	

	def __unicode__(self):
		return '%s'%(self.descripcionMenu)


class Permisos(models.Model):
	rolPermiso = models.ForeignKey(Rol)
	menuPermiso = models.ForeignKey(Menu)