# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-16 21:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='idcliente',
            new_name='idfoto',
        ),
    ]
