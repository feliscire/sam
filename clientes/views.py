# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from clientes.models import Cliente, Photo
from django.core.urlresolvers import reverse_lazy
from clientes.forms import Formulario, FormularioContacto, ClienteForm, ClienteFotoForm
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

def index(request):
    return HttpResponse("Base de Clientes")

def cliente(request):
	cliente_list = Cliente.objects.all()
	context = {'objects_list': cliente_list}
	return render(request, 'clientes/cliente.html', context)

def foto(request, cliente_id):
	cliente = Cliente.objects.get(pk=cliente_id)
	context = {'objects': cliente}
	return render(request, 'clientes/foto.html', context)

def foto2(request, cliente_id):
	cliente = Cliente.objects.get(pk=cliente_id)
	context = {'objects': cliente}
	return render(request, 'clientes/foto2.html', context)

def base(request):
    return render(request, 'base.html')

#def crear_cliente(request):
#	return render(request, 'crear_cliente.html')

#def modif_cliente(request, cliente_id):
#	cliente = Cliente.objects.get(pk=cliente_id)
#	context = {'objects': cliente}
#	return render(request, 'clientes/modif_cliente.html', context)

def contacto(request):
	if request.method == 'POST': # Si el formulario es enviado
		form = Formulario(request.POST) #
		if form.is_valid(): # Si es valido se procesan los datos...
			return HttpResponseRedirect('/clientes/list/gracias/') # y redirige a ... graqcias sino..
	else:
		form = Formulario() # un formulario vacio
	return render(request, 'clientes/contacto.html', {'form': form,})

def gracias(request):
	html = '<html><body><p>"Gracias por enviarnos su comentario..."</p><a href="/clientes/">Listado de Clientes</a></body></html>'
	return HttpResponse(html)

def bootstrap(request):
	return render(request, 'clientes/bootstrap.html')

def contactomail(request):
	if request.method =='POST':
		formulario = FormularioContacto(request.POST)
		if formulario.is_valid():
			correo = formulario.cleaned_data['correo']
			asunto = 'Este es un mensaje de mi blog en Django'
			mensaje = formulario.cleaned_data['mensaje']
			mail = EmailMessage(asunto, mensaje, to=[correo])
			mail.send()
		return HttpResponseRedirect('/clientes/list/gracias/')
	else:
		formulario = FormularioContacto()

	return render(request,'clientes/contacto_mail.html', {'formulario': formulario,})

def cliente_view(request):
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
		    form.save()
		return HttpResponseRedirect('/clientes/list/gracias/')
	else:
		form = ClienteForm()
	return render(request, 'clientes/cliente_form.html', {'form': form})

def cliente_list(request):
	cliente = Cliente.objects.all().order_by('nombre')
	contexto = {'clientes':cliente}
	return render(request, 'clientes/cliente_list.html', contexto)

def cliente_edit(request, cliente_id):
	cliente = Cliente.objects.get(pk=cliente_id)
	if request.method == 'GET':
		form = ClienteForm(instance=cliente)
	else:
		form = ClienteForm(request.POST, instance=cliente)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/clientes/list/listar') 
	return render(request, 'clientes/cliente_form.html', {'form':form})

def cliente_delete(request, cliente_id):
	cliente = Cliente.objects.get(pk=cliente_id)
	if request.method == 'POST':
		cliente.delete()
		return HttpResponseRedirect('/clientes/list/listar')
	return render(request, 'clientes/cliente_delete.html', {'cliente':cliente})

class ClienteList(ListView):
	model = Cliente
	template_name = 'clientes/cliente_list.html'

class ClienteCreate(CreateView):
	model = Cliente
	form_class = ClienteForm
	template_name = 'clientes/cliente_form.html'
	success_url = reverse_lazy('cliente_listar')

class ClienteUpdate(UpdateView):
	model = Cliente
	form_class = ClienteForm
	template_name = 'clientes/cliente_form.html'
	success_url = reverse_lazy('cliente_listar')

class ClienteDelete(DeleteView):
	model = Cliente
	template_name = 'clientes/cliente_delete.html'
	success_url = reverse_lazy('cliente_listar')

class PhotoList(ListView):
	model = Photo
	template_name = 'clientes/photo_list.html'

class PhotoCreate(CreateView):
	model = Photo
	form_class = ClienteFotoForm
	template_name = 'clientes/photo_form.html'
	second_form_class = ClienteForm
	success_url = reverse_lazy('photo_listar')

	def get_context_data(self, **kwargs):
		context = super(PhotoCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = sefl.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			photo = form.save(commit=False)
			photo.cliente = form2.save()
			photo.save()
			return HttpResponseRedirect(self.get_sucess_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))