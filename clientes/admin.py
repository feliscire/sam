from django.contrib import admin
from clientes.models import Cliente, Detalleventa, Producto, Venta, Photo

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_nacimiento','estado',)
    list_filter = ('apellido',)
    ordering = ('apellido',)
    search_fields = ('nombre',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio',)
    list_filter = ('nombre',)
    ordering = ('nombre',)
    search_fields = ('nombre',)

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Detalleventa)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta)
admin.site.register(Photo)