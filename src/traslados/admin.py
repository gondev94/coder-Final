from django.contrib import admin
from . import models


admin.site.register(models.Categoria) 

@admin.register(models.Paquete)
class PaqueteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'distancia', 'categoria')

    
@admin.register(models.Cotizacion)
class CotizacionAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'descripcion', 'precio_por_km', 'paquete', 'total', 'fecha_de_entrega')


@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'direccion', 'telefono', 'email', 'paquete')


@admin.register(models.Flete)
class FleteAdmin(admin.ModelAdmin):
    list_display = ('cliente',)


@admin.register(models.Transportista)
class TransportistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'licencia', 'telefono', 'email', 'flete')
