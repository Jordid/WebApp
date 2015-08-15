# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbonosCuentaCobrar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaAbonoCuentaCobrar', models.DateField()),
                ('montoAbonoCuentaCobrar', models.DecimalField(max_digits=20, decimal_places=2)),
                ('saldoAbonoCuentaCobrar', models.DecimalField(max_digits=20, decimal_places=2)),
                ('numeroReciboAbonoCuentaCobrar', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AbonosCuentaPagar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaAbonoCuentaPagar', models.DateField(auto_now=True)),
                ('montoAbonoCuentaPagar', models.DecimalField(max_digits=20, decimal_places=2)),
                ('saldoAbonoCuentaPagar', models.DecimalField(max_digits=20, decimal_places=2)),
                ('observacionAbonoCuentaPagar', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Aviso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipoAviso', models.CharField(max_length=50)),
                ('descripcionAviso', models.CharField(max_length=400)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcionCategoria', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreCiudad', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estadoCliente', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CuentaCobrar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numeroCuentaCobrar', models.IntegerField(default=0)),
                ('fechaCuetaCobrar', models.DateField(auto_now=True)),
                ('fechaInicioPagoCuentaCobrar', models.DateField(auto_now=True)),
                ('cuotaInicialCuentaCobrar', models.DecimalField(max_digits=20, decimal_places=2)),
                ('cuotaCuentaCobrar', models.DecimalField(max_digits=20, decimal_places=2)),
                ('formaPagoCuentaCobrar', models.CharField(max_length=10)),
                ('totalCuentaCobrar', models.DecimalField(max_digits=20, decimal_places=2)),
                ('saldoCuentaCobrar', models.DecimalField(max_digits=20, decimal_places=2)),
                ('observacionCuentaCobrar', models.TextField()),
                ('estadoCuentaCobrar', models.CharField(max_length=20)),
                ('idCiudadCuentaCobrar', models.ForeignKey(to='app.Ciudad')),
                ('idPersonaCuentaCobrar', models.ForeignKey(to='app.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CuentaPagar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numeroCuentaPagar', models.IntegerField()),
                ('fechaCuentaPagar', models.DateField()),
                ('cuotaInicialCuentaPagar', models.DecimalField(max_digits=20, decimal_places=2)),
                ('cuotasCuentaPagar', models.DecimalField(max_digits=20, decimal_places=2)),
                ('totalCuentaPagar', models.DecimalField(max_digits=20, decimal_places=2)),
                ('saldoCuentaPagar', models.DecimalField(max_digits=20, decimal_places=2)),
                ('observacionCuentaPagar', models.TextField()),
                ('estadoCuentaPagar', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DatosEmpresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreDatosEmpresa', models.CharField(max_length=50)),
                ('direccionDatosEmpresa', models.CharField(max_length=100)),
                ('telefonoDatosEmpresa', models.CharField(max_length=21)),
                ('misionDatosEmpresa', models.TextField()),
                ('visionDatosEmpresa', models.TextField()),
                ('nuestrosProductosDatosEmpresa', models.TextField()),
                ('quienesSomosDatosEmpresa', models.TextField()),
                ('logoDatosEmpresa', models.URLField()),
                ('emailDatosEmpresa', models.EmailField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetalleCuentaCobrar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidadDetCueCob', models.DecimalField(max_digits=20, decimal_places=2)),
                ('precioDetCueCob', models.DecimalField(max_digits=20, decimal_places=2)),
                ('idCuentaCobrarDetCueCob', models.ForeignKey(to='app.CuentaCobrar')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidadDetalleFactura', models.DecimalField(max_digits=20, decimal_places=2)),
                ('precioDetalleFactura', models.DecimalField(max_digits=20, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cargoEmpleado', models.CharField(max_length=50)),
                ('estadoEmpleado', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numeroFactura', models.IntegerField()),
                ('fechaFactura', models.DateField(auto_now=True)),
                ('subtotalFactura', models.DecimalField(max_digits=20, decimal_places=2)),
                ('descuentoFactura', models.DecimalField(max_digits=20, decimal_places=2)),
                ('ivaCeroFactura', models.DecimalField(max_digits=20, decimal_places=2)),
                ('ivaDoceFactura', models.DecimalField(max_digits=20, decimal_places=2)),
                ('totalFactura', models.DecimalField(max_digits=20, decimal_places=2)),
                ('estadoFactura', models.CharField(max_length=20)),
                ('idDatosEmpresaFactura', models.ForeignKey(to='app.DatosEmpresa')),
                ('idPersonaFactura', models.ForeignKey(to='app.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kardex',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaKardex', models.DateTimeField(auto_now=True)),
                ('cantidadKardex', models.DecimalField(max_digits=20, decimal_places=2)),
                ('precioUnitarioKardex', models.DecimalField(max_digits=20, decimal_places=2)),
                ('saldoKardex', models.DecimalField(max_digits=20, decimal_places=2)),
                ('razonKardex', models.CharField(max_length=5)),
                ('observacionesKardex', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigoMenu', models.CharField(max_length=20)),
                ('descripcionMenu', models.TextField()),
                ('posicionMenu', models.IntegerField()),
                ('iconoMenu', models.URLField()),
                ('estadoMenu', models.CharField(max_length=20)),
                ('urlMenu', models.TextField()),
                ('codigoPadreMenu', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notificacione',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaNotificacion', models.DateField()),
                ('observacionNotificacion', models.TextField()),
                ('idAviso', models.ForeignKey(to='app.Aviso')),
                ('idCuentaCobrar', models.ForeignKey(to='app.CuentaCobrar')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idMenuPermiso', models.ForeignKey(to='app.Menu')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedulaPersona', models.CharField(max_length=20)),
                ('apellidosPersona', models.CharField(max_length=50)),
                ('nombresPersona', models.CharField(max_length=50)),
                ('telefonoPersona', models.CharField(max_length=10)),
                ('celularPersona', models.CharField(max_length=10)),
                ('direccionPersona', models.TextField(help_text=b'Redacte la direccion')),
                ('emailPersona', models.EmailField(max_length=50)),
                ('observacionesPersona', models.TextField(help_text=b'Redacte las observaciones')),
                ('idCiudadPersona', models.ForeignKey(to='app.Ciudad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigoProducto', models.CharField(max_length=20)),
                ('descripcionProducto', models.TextField()),
                ('cantidadProducto', models.DecimalField(max_digits=20, decimal_places=2)),
                ('stockMinimoProducto', models.DecimalField(max_digits=20, decimal_places=2)),
                ('costoProducto', models.DecimalField(max_digits=20, decimal_places=2)),
                ('valorAgregadoProducto', models.DecimalField(max_digits=20, decimal_places=2)),
                ('ivaProducto', models.DecimalField(max_digits=20, decimal_places=2)),
                ('precioContadoProducto', models.DecimalField(max_digits=20, decimal_places=2)),
                ('precioCreditoProducto', models.DecimalField(max_digits=20, decimal_places=2)),
                ('estadoProducto', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estadoProveedor', models.CharField(max_length=20)),
                ('idPersonaProveedor', models.ForeignKey(to='app.Persona')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreProvincia', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreRol', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickUsuario', models.CharField(max_length=20)),
                ('claveUsuario', models.TextField()),
                ('fechaUltimoAccesoUsuario', models.DateField()),
                ('estadoUsuario', models.CharField(max_length=20)),
                ('idPersonaUsuario', models.ForeignKey(to='app.Persona')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UsuarioRoles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idPersona', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('idRol', models.ForeignKey(to='app.Rol')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='permisos',
            name='idRolPermiso',
            field=models.ForeignKey(to='app.Rol'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kardex',
            name='idPersonaKardex',
            field=models.ForeignKey(to='app.Persona'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kardex',
            name='idProductoKardex',
            field=models.ForeignKey(to='app.Producto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='empleado',
            name='idPersonaEmpleado',
            field=models.ForeignKey(to='app.Persona'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='idFacturaDetalleFactura',
            field=models.ForeignKey(to='app.Factura'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='idProductoDetalleFactura',
            field=models.ForeignKey(to='app.Producto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detallecuentacobrar',
            name='idProductoDetCueCob',
            field=models.ForeignKey(to='app.Producto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cuentapagar',
            name='idPersonaCuentaPagar',
            field=models.ForeignKey(to='app.Proveedor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='idPersonaCliente',
            field=models.ForeignKey(to='app.Persona'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ciudad',
            name='idProvinciaCiudad',
            field=models.ForeignKey(to='app.Provincia'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abonoscuentapagar',
            name='idCuentaPagarAbonoCuentaPagar',
            field=models.ForeignKey(to='app.CuentaPagar'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abonoscuentacobrar',
            name='idCuentaCobrarAbonoCuentaCobrar',
            field=models.ForeignKey(to='app.CuentaCobrar'),
            preserve_default=True,
        ),
    ]
