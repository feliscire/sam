# -*- coding: utf-8 -*-
from django import forms
from clientes.models import Cliente, Photo

class FormularioContacto(forms.Form):
	correo = forms.EmailField()
	mensaje = forms.CharField()

class Formulario(forms.Form):
    # se define como un modelo
    nombre = forms.CharField(max_length=100)
    mensaje = forms.CharField()
    mail = forms.EmailField()

class ClienteForm(forms.ModelForm):

    class Meta:
    	model = Cliente

    	fields = [
    		'nombre',
    		'apellido',
    		'fecha_nacimiento',
    		'direccion',
    		'estado',
    		'kg',
    	]
    	label = {
    		'nombre': 'Nombre',
    		'apellido': 'Apellido',
    		'fecha_nacimiento': 'Fecha de Nacimiento',
    		'direccion': 'Direccion',
    		'estado': 'Estado',
    		'kg': 'Peso Aproximado',
    	}
    	widget = {
    	    'nombre': forms.TextInput(attrs={'class': 'form-control'}),
    		'apellido': forms.TextInput(attrs={'class': 'form-control'}),
    		'fecha_nacimiento': forms.DateField(required=True),
    		'direccion': forms.TextInput(attrs={'class': 'form-control'}),
    		'estado': forms.TextInput(attrs={'class': 'form-control'}),
    		'kg': forms.TextInput(attrs={'class': 'form-control'}),
    	}

class ClienteFotoForm(forms.ModelForm):

    class Meta:
    	model = Photo

    	fields = [
    		'idfoto',
    		'title',
    		'photo',
    		#'pub_date',
    		'favorite',
    		'comment',
    	]
    	label = {
    		'idfoto': 'Indice',
    		'title': 'Titulo',
    		'photo': 'Nombre de Foto',
    		#'pub_date': 'Fecha de Publicacion',
    		'favorite': 'Favorito',
    		'comment': 'Comentario',
    	}
    	widget = {
    	    'idfoto': forms.TextInput(attrs={'class': 'form-control'}),
    		'title': forms.TextInput(attrs={'class': 'form-control'}),
    		'photo': forms.ImageField(),
    		#'pub_date': forms.DateField(auto_now_add=True),
    		'favorite': forms.TextInput(attrs={'class': 'form-control'}),
    		'comment': forms.TextInput(attrs={'class': 'form-control'}),
    	}