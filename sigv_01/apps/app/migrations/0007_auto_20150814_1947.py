# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_datosempresa_ciudaddatosempresa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosempresa',
            name='ciudadDatosEmpresa',
        ),
        migrations.AddField(
            model_name='factura',
            name='observacionesFactura',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
