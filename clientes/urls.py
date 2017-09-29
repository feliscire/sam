from django.conf.urls import url

from . import views
from clientes.views import ClienteList, ClienteCreate, ClienteUpdate, ClienteDelete, PhotoList, PhotoCreate

urlpatterns = [
    url(r'^admin$', views.cliente_admin, name="cliente_admin"),
    #url(r'^list/nuevo$', views.cliente_view, name='cliente_crear'),
    url(r'^nuevo$', ClienteCreate.as_view(), name='cliente_crear'),
    #url(r'^list/listar$', views.cliente_list, name='cliente_listar'),
    url(r'^listar$', ClienteList.as_view(), name='cliente_listar'),
    #url(r'^list/editar/(?P<cliente_id>\d+)/$', views.cliente_edit, name='cliente_editar'),
    url(r'^editar/(?P<pk>\d+)/$', ClienteUpdate.as_view(), name='cliente_editar'),
    #url(r'^list/eliminar/(?P<cliente_id>\d+)/$', views.cliente_delete, name='cliente_eliminar'),
    url(r'^eliminar/(?P<pk>\d+)/$', ClienteDelete.as_view(), name='cliente_eliminar'),
    
    url(r'^photo/listar$', PhotoList.as_view(), name='photo_listar'),
    url(r'^photo/nuevo$', PhotoCreate.as_view(), name='photo_crear'),

    url(r'^$', views.base, name='base'),
    #url(r'^/list/boot$', views.bootstrap, name='bootstrap'),

    url(r'^list/contacto/$', views.contacto, name='contacto'),
    url(r'^list/gracias/$', views.gracias, name='gracias'),

    url(r'^list/contactomail/$', views.contactomail, name='contactomail'),

    url(r'^list/$', views.cliente, name='cliente-list'),
    url(r'^list/(?P<cliente_id>\d+)/foto/$', views.foto, name='cliente-foto'),
    url(r'^list/(?P<cliente_id>\d+)/foto2/$', views.foto2, name='cliente-foto2'),
]