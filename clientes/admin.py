# Importamos las herramientas necesarias del administrador de Django
from django.contrib import admin

# Importamos los modelos que queremos registrar en el panel de administración
from .models import Cliente, Interes

admin.site.register(Cliente)
admin.site.register(Interes)


