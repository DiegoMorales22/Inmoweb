from django.urls import path
from . import views

urlpatterns = [
    path('',views.lista_propiedades, name='propiedades'),
    path('agentes/',views.lista_Agentes, name='agentes'),
    path('registroPropiedad/',views.RegistroPropiedad, name='registroPropiedad'),
    path('registroExitoso/',views.registroExitoso, name='registroExitoso'), 
    path('editar/<int:id>/',views.editar_propiedad, name='editar_propiedad'),
    path('eliminar/<int:id>/', views.eliminar_propiedad, name='eliminar_propiedad')
]
