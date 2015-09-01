# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20150829_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonocuentacobrar',
            name='fechaAbonoCuentaCobrar',
            field=models.DateField(default=datetime.datetime(2015, 8, 29, 14, 53, 57, 857000)),
        ),
        migrations.AlterField(
            model_name='abonocuentapagar',
            name='fechaAbonoCuentaPagar',
            field=models.DateField(default=datetime.datetime(2015, 8, 29, 14, 53, 57, 857000)),
        ),
        migrations.AlterField(
            model_name='cuentacobrar',
            name='fechaCuetaCobrar',
            field=models.DateField(default=datetime.datetime(2015, 8, 29, 14, 53, 57, 841000)),
        ),
        migrations.AlterField(
            model_name='cuentacobrar',
            name='fechaInicioPagoCuentaCobrar',
            field=models.DateField(default=datetime.datetime(2015, 8, 29, 14, 53, 57, 841000)),
        ),
        migrations.AlterField(
            model_name='cuentapagar',
            name='fechaCuentaPagar',
            field=models.DateField(default=datetime.datetime(2015, 8, 29, 14, 53, 57, 857000)),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fechaFactura',
            field=models.DateField(default=datetime.datetime(2015, 8, 29, 14, 53, 57, 857000)),
        ),
        migrations.AlterField(
            model_name='kardex',
            name='fechaKardex',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 29, 14, 53, 57, 841000)),
        ),
        migrations.AlterField(
            model_name='notificacion',
            name='fechaNotificacion',
            field=models.DateField(default=datetime.datetime(2015, 8, 29, 14, 53, 57, 841000)),
        ),
    ]
