from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

from .models import Propiedad, Agente
from django.http import HttpResponse
from .forms import RegistrarPropiedad

# Create your views here.

def lista_propiedades(request):
    propiedades = Propiedad.objects.all()

    ciudad = request.GET.get('ciudad')
    tipo = request.GET.get('tipo')
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')

    if ciudad:
        propiedades = propiedades.filter(ciudad__icontains=ciudad)  # busca aunque no coincida exacto
    if tipo:
        propiedades = propiedades.filter(tipo=tipo)
    if precio_min:
        propiedades = propiedades.filter(precio__gte=precio_min)  # gte = mayor o igual que
    if precio_max:
        propiedades = propiedades.filter(precio__lte=precio_max)  # lte = menor o igual que

    return render(request, 'propiedades/lista_propiedades.html', {'propiedades': propiedades})


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

def editar_propiedad(request,id):
    propiedad=get_object_or_404(Propiedad, id=id) #traeme la propiedad que tenga ese id y si no existe muestrame un error 404
    if request.method=='POST':
          form = RegistrarPropiedad(request.POST,request.FILES,instance=propiedad) 
          if form.is_valid():
               form.save()
               return redirect('lista_propiedades')
    else:
         form=RegistrarPropiedad(instance=propiedad)
    return render(request,'propiedades/editar_propiedad.html', {'form': form, 'propiedad': propiedad})

def eliminar_propiedad(request,id):
     propiedad = get_object_or_404(Propiedad, id=id)
     propiedad.delete()
     return redirect('lista_propiedades')
          
"""
🧩 Retos para ti (de más fácil a más desafiante)
💡 Reto 1: Mostrar propiedad por id

Crea una vista llamada ver_propiedad que:

Reciba un parámetro id.

Use get_object_or_404(Propiedad, id=id).

Muestre los datos de esa propiedad en un template ver_propiedad.html.

🧠 Objetivo: practicar cómo obtener y enviar un objeto al template.
"""
def ver_propiedad(request,id):
     propiedad = get_object_or_404(Propiedad, id=id)
     return render(request, 'propiedades/ver_propiedad.html', {"propiedad":propiedad})

