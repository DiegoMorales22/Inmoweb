from django.urls import path
from . import views

urlpatterns= [
    path('registro/', views.registrar_cliente, name='clientes_registro'),
    path('registro-exitoso/', views.registro_exitoso, name='registro_exitoso'),
   
    
]
