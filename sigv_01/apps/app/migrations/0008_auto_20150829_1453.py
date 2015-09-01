# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150814_1947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='observacionesEmpledo',
            new_name='observacionesEmpleado',
        ),
        migrations.RenameField(
            model_name='usuarioroles',
            old_name='usuarioUsurioRoles',
            new_name='usuarioUsuarioRoles',
        ),
        migrations.AddField(
            model_name='abonocuentacobrar',
            name='observacionesAbonoCuentaCobrar',
            field=models.TextField(default=b'', help_text=b'Redacte las observaciones'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datosempresa',
            name='ciudadDatosEmpresa',
            field=models.ForeignKey(default=1, to='app.Ciudad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datosempresa',
            name='claveDatosEmpresa',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='factura',
            name='esCuentaCobrarFactura',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='paqueteMenu',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='observacionesProveedor',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abonocuentacobrar',
            name='fechaAbonoCuentaCobrar',
            field=models.DateField(default=datetime.datetime(2015, 8, 29, 14, 53, 7, 392000)),
        ),
        migrations.AlterField(
            model_name='abonocuentapagar',
            name='fechaAbonoCuentaPagar',
            field=models.DateField(default=datetime.datetime(2015, 8, 29, 14, 53, 7, 392000)),
        ),
        migrations.AlterField(
            model_name='cuentacobrar',
            name='fechaCuetaCobrar',
            field=models.DateField(default=datetime.datetime(2015, 8, 29, 14, 53, 7, 392000)),
        ),
        migrations.AlterField(
            model_name='cuentacobrar',
            name='fechaInicioPagoCuentaCobrar',
            field=models.DateField(default=datetime.datetime(2015, 8, 29, 14, 53, 7, 392000)),
        ),
        migrations.AlterField(
            model_name='cuentapagar',
            name='fechaCuentaPagar',
            field=models.DateField(default=datetime.datetime(2015, 8, 29, 14, 53, 7, 392000)),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fechaFactura',
            field=models.DateField(default=datetime.datetime(2015, 8, 29, 14, 53, 7, 392000)),
        ),
        migrations.AlterField(
            model_name='kardex',
            name='fechaKardex',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 29, 14, 53, 7, 392000)),
        ),
        migrations.AlterField(
            model_name='notificacion',
            name='fechaNotificacion',
            field=models.DateField(default=datetime.datetime(2015, 8, 29, 14, 53, 7, 392000)),
        ),
    ]
