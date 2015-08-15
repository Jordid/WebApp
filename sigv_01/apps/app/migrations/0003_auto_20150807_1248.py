# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150723_2120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuarioroles',
            old_name='rol',
            new_name='rolUsuarioRoles',
        ),
        migrations.RemoveField(
            model_name='usuarioroles',
            name='persona',
        ),
        migrations.AddField(
            model_name='usuarioroles',
            name='usuarioUsurioRoles',
            field=models.ForeignKey(default=0, to='app.Usuario'),
            preserve_default=False,
        ),
    ]
