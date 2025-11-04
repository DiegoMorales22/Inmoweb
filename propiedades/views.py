from django.shortcuts import render,redirect
from .models import Propiedad, Agente
from django.http import HttpResponse
from .forms import RegistrarPropiedad
# Create your views here.

def lista_propiedades(request):
    propiedades = Propiedad.objects.all()# aqui muestro todas las propiedades 
    return render(request,'propiedades/propiedades.html' ,{'propiedades': propiedades})

def lista_Agentes(request):
    agentes = Agente.objects.all()# aqui mostrare toda la lista de agentes
    return render(request, 'propiedades/agentes.html',{'agentes': agentes})


def RegistroPropiedad(request):
    if request.method=="POST": # cuando el usuario envia ya diligenciado el formulario se Valida-Se Guarda
        form= RegistrarPropiedad(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registroExitoso')
    else:
            form= RegistrarPropiedad()# cuando el usuario entra le muestro el formulario vacio
    return render(request,'propiedades/registroPropiedad.html',{"form":form})

def registroExitoso(request):
    return render(request,'propiedades/registroexitoso.html')



