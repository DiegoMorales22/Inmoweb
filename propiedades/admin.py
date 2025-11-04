from django.contrib import admin
from .models import Propiedad,Agente

admin.site.register(Agente)
@admin.register(Propiedad,)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ciudad", "precio", "tipo", "fecha_publicacion")#sirve para filtar las busquedas en el admin
    search_fields = ("titulo", "ciudad")
    list_filter = ("tipo", "ciudad")

