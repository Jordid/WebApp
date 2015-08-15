# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbonoCuentaCobrar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaAbonoCuentaCobrar', models.DateField(auto_now=True)),
                ('montoAbonoCuentaCobrar', models.DecimalField(max_digits=20, decimal_places=2)),
                ('saldoAbonoCuentaCobrar', models.DecimalField(max_digits=20, decimal_places=2)),
                ('numeroReciboAbonoCuentaCobrar', models.IntegerField(default=0)),
                ('cuentaCobrarAbonoCuentaCobrar', models.ForeignKey(to='app.CuentaCobrar')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AbonoCuentaPagar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaAbonoCuentaPagar', models.DateField(auto_now=True)),
                ('montoAbonoCuentaPagar', models.DecimalField(max_digits=20, decimal_places=2)),
                ('saldoAbonoCuentaPagar', models.DecimalField(max_digits=20, decimal_places=2)),
                ('observacionesAbonoCuentaPagar', models.TextField(default=b'', help_text=b'Redacte las observaciones')),
                ('cuentaPagarAbonoCuentaPagar', models.ForeignKey(to='app.CuentaPagar')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaNotificacion', models.DateField(auto_now=True)),
                ('observacionesNotificacion', models.TextField(default=b'', help_text=b'Redacte las observaciones')),
                ('aviso', models.ForeignKey(to='app.Aviso')),
                ('cuentaCobrar', models.ForeignKey(to='app.CuentaCobrar')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='abonoscuentacobrar',
            name='idCuentaCobrarAbonoCuentaCobrar',
        ),
        migrations.DeleteModel(
            name='AbonosCuentaCobrar',
        ),
        migrations.RemoveField(
            model_name='abonoscuentapagar',
            name='idCuentaPagarAbonoCuentaPagar',
        ),
        migrations.DeleteModel(
            name='AbonosCuentaPagar',
        ),
        migrations.RemoveField(
            model_name='notificacione',
            name='idAviso',
        ),
        migrations.RemoveField(
            model_name='notificacione',
            name='idCuentaCobrar',
        ),
        migrations.DeleteModel(
            name='Notificacione',
        ),
        migrations.RenameField(
            model_name='ciudad',
            old_name='idProvinciaCiudad',
            new_name='provinciaCiudad',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='idPersonaCliente',
            new_name='personaCliente',
        ),
        migrations.RenameField(
            model_name='cuentacobrar',
            old_name='idCiudadCuentaCobrar',
            new_name='ciudadCuentaCobrar',
        ),
        migrations.RenameField(
            model_name='cuentacobrar',
            old_name='idPersonaCuentaCobrar',
            new_name='clienteCuentaCobrar',
        ),
        migrations.RenameField(
            model_name='cuentapagar',
            old_name='idPersonaCuentaPagar',
            new_name='personaCuentaPagar',
        ),
        migrations.RenameField(
            model_name='detallecuentacobrar',
            old_name='idCuentaCobrarDetCueCob',
            new_name='cuentaCobrarDetCueCob',
        ),
        migrations.RenameField(
            model_name='detallecuentacobrar',
            old_name='idProductoDetCueCob',
            new_name='productoDetCueCob',
        ),
        migrations.RenameField(
            model_name='detallefactura',
            old_name='idFacturaDetalleFactura',
            new_name='facturaDetalleFactura',
        ),
        migrations.RenameField(
            model_name='detallefactura',
            old_name='idProductoDetalleFactura',
            new_name='productoDetalleFactura',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='idPersonaEmpleado',
            new_name='personaEmpleado',
        ),
        migrations.RenameField(
            model_name='factura',
            old_name='idPersonaFactura',
            new_name='clienteFactura',
        ),
        migrations.RenameField(
            model_name='factura',
            old_name='idDatosEmpresaFactura',
            new_name='datosEmpresaFactura',
        ),
        migrations.RenameField(
            model_name='kardex',
            old_name='idPersonaKardex',
            new_name='personaKardex',
        ),
        migrations.RenameField(
            model_name='kardex',
            old_name='idProductoKardex',
            new_name='productoKardex',
        ),
        migrations.RenameField(
            model_name='permisos',
            old_name='idMenuPermiso',
            new_name='menuPermiso',
        ),
        migrations.RenameField(
            model_name='permisos',
            old_name='idRolPermiso',
            new_name='rolPermiso',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='idCiudadPersona',
            new_name='ciudadPersona',
        ),
        migrations.RenameField(
            model_name='proveedor',
            old_name='idPersonaProveedor',
            new_name='personaProveedor',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='idPersonaUsuario',
            new_name='personaUsuario',
        ),
        migrations.RenameField(
            model_name='usuarioroles',
            old_name='idPersona',
            new_name='persona',
        ),
        migrations.RenameField(
            model_name='usuarioroles',
            old_name='idRol',
            new_name='rol',
        ),
        migrations.RemoveField(
            model_name='cuentacobrar',
            name='observacionCuentaCobrar',
        ),
        migrations.RemoveField(
            model_name='cuentapagar',
            name='observacionCuentaPagar',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='celularPersona',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='observacionesPersona',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='fechaUltimoAccesoUsuario',
        ),
        migrations.AddField(
            model_name='cliente',
            name='observacionesCliente',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cuentacobrar',
            name='observacionesCuentaCobrar',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cuentapagar',
            name='observacionesCuentaPagar',
            field=models.TextField(default=b'', help_text=b'Redacte las observaciones'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='empleado',
            name='observacionesEmpledo',
            field=models.TextField(default=b'', help_text=b'Redacte las observaciones'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producto',
            name='categoriaProducto',
            field=models.ForeignKey(default=1, to='app.Categoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='marcaProducto',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aviso',
            name='descripcionAviso',
            field=models.TextField(default=b'', help_text=b'Redacte las observaciones'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='descripcionCategoria',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='nombreCiudad',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cuentapagar',
            name='fechaCuentaPagar',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='cuentapagar',
            name='numeroCuentaPagar',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='datosempresa',
            name='logoDatosEmpresa',
            field=models.URLField(default=b''),
        ),
        migrations.AlterField(
            model_name='datosempresa',
            name='misionDatosEmpresa',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='datosempresa',
            name='nuestrosProductosDatosEmpresa',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='datosempresa',
            name='quienesSomosDatosEmpresa',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='datosempresa',
            name='visionDatosEmpresa',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='factura',
            name='numeroFactura',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='kardex',
            name='observacionesKardex',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='menu',
            name='descripcionMenu',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='menu',
            name='posicionMenu',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='menu',
            name='urlMenu',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='provincia',
            name='nombreProvincia',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='claveUsuario',
            field=models.TextField(default=b''),
        ),
    ]
