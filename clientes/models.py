# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

class Cliente(models.Model):
    idcliente = models.AutoField(db_column='IdCliente', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=45)  # Field name made lowercase.
    fecha_nacimiento = models.DateField(db_column='Fecha_Nacimiento', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(max_length=2)
    kg = models.IntegerField(db_column='KG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientes'

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

class Detalleventa(models.Model):
    iddetalle = models.AutoField(db_column='IdDetalle', primary_key=True)  # Field name made lowercase.
    idventa = models.ForeignKey('Venta', models.DO_NOTHING, db_column='IdVenta')  # Field name made lowercase.
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='IdProducto')  # Field name made lowercase.
    cantidad = models.IntegerField()
    descuento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.cantidad, self.descuento)

    class Meta:
        managed = False
        db_table = 'detalleventa'

class Producto(models.Model):
    idproductos = models.AutoField(db_column='IdProductos', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return '%s %s' % (self.nombre, self.precio)

    class Meta:
        managed = False
        db_table = 'productos'

class Venta(models.Model):
    idventa = models.AutoField(db_column='IdVenta', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='IdCliente')  # Field name made lowercase.
    
    class Admin:
        list_display = ('idventa', 'idcliente', 'fecha')
        list_filter = ('fecha')
        ordering = ('fecha',)
        search_fields = ('fecha',)
    
    def __date__(self):
        return self.fecha

    class Meta:
        managed = False
        db_table = 'ventas'

class Photo(models.Model):
    """ Fotos del album """
    idfoto = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='IdCliente')  # Field name made lowercase.
    title = models.CharField(max_length=50, default='No title')
    photo = models.ImageField(upload_to='photos/')
    pub_date = models.DateField(auto_now_add=True)
    favorite = models.BooleanField(default=False)
    comment = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cliente-foto2')

@receiver(post_delete, sender=Photo)
def photo_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.photo.delete(False)