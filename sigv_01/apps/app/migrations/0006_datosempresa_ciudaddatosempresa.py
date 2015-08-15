# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_factura_ciudadfactura'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosempresa',
            name='ciudadDatosEmpresa',
            field=models.ForeignKey(default=1, to='app.Ciudad'),
            preserve_default=False,
        ),
    ]
