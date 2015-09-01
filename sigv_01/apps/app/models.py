from django.db import models
from datetime import datetime
# Create your models here.
#Ok
class Provincia(models.Model):
	nombreProvincia = models.CharField(max_length = 100)

	def __unicode__(self):
		return '%s'%(self.nombreProvincia)
#Ok
class Ciudad(models.Model):
	nombreCiudad = models.CharField(max_length = 100)
	provinciaCiudad = models.ForeignKey(Provincia)

	def __unicode__(self):
		return '%s'%(self.nombreCiudad)

#Ok
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
#Ok
class Empleado(models.Model):
	cargoEmpleado = models.CharField(max_length = 50)
	observacionesEmpleado = models.TextField(default="", help_text = 'Redacte las observaciones')
	estadoEmpleado = models.CharField(max_length=20)
	personaEmpleado = models.ForeignKey(Persona)

#Ok
class Proveedor(models.Model):
	estadoProveedor = models.CharField(max_length = 20)
	personaProveedor = models.ForeignKey(Persona)
	observacionesProveedor = models.TextField(default="")
#Ok
class Cliente(models.Model):
	estadoCliente = models.CharField(max_length = 20)
	observacionesCliente = models.TextField(default="")
	personaCliente = models.ForeignKey(Persona)
#Ok
class Usuario(models.Model):
	nickUsuario = models.CharField(max_length=20)
	claveUsuario = models.TextField(default="")
	estadoUsuario = models.CharField(max_length=20)
	personaUsuario = models.ForeignKey(Persona)	

	def __unicode__(self):
		return '%s'%(self.nickUsuario)

#-------Seccion Bodega-------#
class Categoria(models.Model):
	descripcionCategoria = models.CharField(max_length = 100)

	def __unicode__(self):
		return '%s'%(self.descripcionCategoria)
#Ok
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

#Ok
class Kardex(models.Model):
	fechaKardex = models.DateTimeField(default=datetime.now())
	cantidadKardex = models.DecimalField(max_digits = 20,decimal_places = 2)
	precioUnitarioKardex = models.DecimalField(max_digits = 20,decimal_places = 2)
	saldoKardex = models.DecimalField(max_digits = 20,decimal_places = 2)
	razonKardex = models.CharField(max_length = 5)
	observacionesKardex = models.TextField(default="")
	personaKardex = models.ForeignKey(Persona)
	productoKardex = models.ForeignKey(Producto)
#Ok
class Aviso(models.Model):
	tipoAviso = models.CharField(max_length=50)
	descripcionAviso = models.TextField(default="", help_text = 'Redacte las observaciones')
#Ok
class CuentaCobrar(models.Model):
	numeroCuentaCobrar = models.IntegerField(default = 0)
	fechaCuetaCobrar = models.DateField(default=datetime.now())
	fechaInicioPagoCuentaCobrar = models.DateField(default=datetime.now())
	cuotaInicialCuentaCobrar = models.DecimalField(max_digits = 20,decimal_places = 2)
	cuotaCuentaCobrar = models.DecimalField(max_digits = 20,decimal_places = 2)
	formaPagoCuentaCobrar = models.CharField(max_length=10)
	totalCuentaCobrar = models.DecimalField(max_digits = 20,decimal_places = 2)
	saldoCuentaCobrar = models.DecimalField(max_digits = 20,decimal_places = 2)
	observacionesCuentaCobrar = models.TextField(default="")
	estadoCuentaCobrar = models.CharField(max_length=20)
	ciudadCuentaCobrar = models.ForeignKey(Ciudad)
	clienteCuentaCobrar = models.ForeignKey(Cliente)
#Ok
class Notificacion(models.Model):
	fechaNotificacion = models.DateField(default=datetime.now())
	observacionesNotificacion = models.TextField(default="", help_text = 'Redacte las observaciones')
	cuentaCobrar = models.ForeignKey(CuentaCobrar)
	aviso = models.ForeignKey(Aviso)
#Ok
class DetalleCuentaCobrar(models.Model):
	cantidadDetCueCob = models.DecimalField(max_digits = 20,decimal_places = 2)
	precioDetCueCob = models.DecimalField(max_digits = 20,decimal_places = 2) 
	cuentaCobrarDetCueCob = models.ForeignKey(CuentaCobrar)
	productoDetCueCob = models.ForeignKey(Producto)
#Ok
class AbonoCuentaCobrar(models.Model):
	fechaAbonoCuentaCobrar = models.DateField(default=datetime.now())
	montoAbonoCuentaCobrar = models.DecimalField(max_digits = 20,decimal_places = 2)
	saldoAbonoCuentaCobrar = models.DecimalField(max_digits = 20,decimal_places = 2)
	numeroReciboAbonoCuentaCobrar = models.IntegerField(default = 0)
	cuentaCobrarAbonoCuentaCobrar = models.ForeignKey(CuentaCobrar)
	observacionesAbonoCuentaCobrar = models.TextField(default="", help_text = 'Redacte las observaciones')
#Ok
class CuentaPagar(models.Model):
	numeroCuentaPagar = models.IntegerField(default=0)
	fechaCuentaPagar = models.DateField(default=datetime.now())
	cuotaInicialCuentaPagar = models.DecimalField(max_digits = 20,decimal_places = 2)
	cuotasCuentaPagar = models.DecimalField(max_digits = 20,decimal_places = 2)
	totalCuentaPagar = models.DecimalField(max_digits = 20,decimal_places = 2)
	saldoCuentaPagar = models.DecimalField(max_digits = 20,decimal_places = 2)
	observacionesCuentaPagar = models.TextField(default="", help_text = 'Redacte las observaciones')
	estadoCuentaPagar = models.CharField(max_length=20)
	personaCuentaPagar = models.ForeignKey(Proveedor)
#Ok
class AbonoCuentaPagar(models.Model):
	fechaAbonoCuentaPagar = models.DateField(default=datetime.now())
	montoAbonoCuentaPagar = models.DecimalField(max_digits = 20,decimal_places = 2)
	saldoAbonoCuentaPagar = models.DecimalField(max_digits = 20,decimal_places = 2)
	observacionesAbonoCuentaPagar = models.TextField(default="", help_text = 'Redacte las observaciones')
	cuentaPagarAbonoCuentaPagar = models.ForeignKey(CuentaPagar)
#Ok
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
	claveDatosEmpresa = models.CharField(max_length=100) 
	ciudadDatosEmpresa = models.ForeignKey(Ciudad)
#Ok
class Factura(models.Model):
	numeroFactura = models.IntegerField(default=0)
	fechaFactura = models.DateField(default=datetime.now())
	subtotalFactura = models.DecimalField(max_digits = 20,decimal_places = 2)
	descuentoFactura = models.DecimalField(max_digits = 20,decimal_places = 2)
	ivaCeroFactura = models.DecimalField(max_digits = 20,decimal_places = 2)
	ivaDoceFactura = models.DecimalField(max_digits = 20,decimal_places = 2)
	totalFactura = models.DecimalField(max_digits = 20,decimal_places = 2)
	estadoFactura = models.CharField(max_length=20)
	observacionesFactura = models.TextField(default="")
	esCuentaCobrarFactura = models.CharField(max_length=2)
	datosEmpresaFactura = models.ForeignKey(DatosEmpresa)
	clienteFactura = models.ForeignKey(Cliente)
	def __unicode__(self):
		return '%s'%(self.numeroFactura)
	class Meta:
		ordering = ["numeroFactura"]
#Ok
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
	usuarioUsuarioRoles = models.ForeignKey(Usuario)
	def __unicode__(self):
		return '%s-%s'%(self.rolUsuarioRoles, self.usuarioUsuarioRoles)

class Menu(models.Model):
	codigoMenu = models.CharField(max_length=20)
	descripcionMenu = models.TextField(default="")
	posicionMenu = models.IntegerField(default=0)
	iconoMenu = models.URLField()
	estadoMenu = models.CharField(max_length=20)
	urlMenu = models.TextField(default="")
	paqueteMenu = models.TextField(default="")
	codigoPadreMenu = models.CharField(max_length=20)	


	def __unicode__(self):
		return '%s'%(self.descripcionMenu)

	class Meta:
		ordering = ["posicionMenu"]


class Permisos(models.Model):
	rolPermiso = models.ForeignKey(Rol)
	menuPermiso = models.ForeignKey(Menu)

	class Meta:
		ordering = ["menuPermiso"]