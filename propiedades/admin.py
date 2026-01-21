from django.contrib import admin
from .models import Propiedad,Agente,MensajeContacto

admin.site.register(Agente)
@admin.register(Propiedad,)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ciudad", "precio", "tipo", "fecha_publicacion")#sirve para filtar las busquedas en el admin
    search_fields = ("titulo", "ciudad")
    list_filter = ("tipo", "ciudad")

@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    # Columnas visibles en la lista
    list_display = (
        'nombre',        # Nombre del usuario
        'email',         # Email
        'propiedad',     # Propiedad relacionada
        'creado',        # Fecha
    )

    # Filtros laterales
    list_filter = (
        'creado',
        'propiedad',
    )

    # Buscador arriba
    search_fields = (
        'nombre',
        'email',
        'mensaje',
    )

    # Orden por defecto (más nuevos primero)
    ordering = ('-creado',)

