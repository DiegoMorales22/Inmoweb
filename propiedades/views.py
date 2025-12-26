from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404


from .models import Propiedad, Agente
from django.http import HttpResponse
from .forms import RegistrarPropiedad

# Create your views here.

def lista_propiedades(request):
    errores = {}
    propiedades = Propiedad.objects.all()

    ciudad = request.GET.get('ciudad', '')
    tipo = request.GET.get('tipo', '')
    precio_min = request.GET.get('precio_min', '')
    precio_max = request.GET.get('precio_max', '')

    # VALIDACIONES
    if ciudad and not ciudad.isalpha():
        errores['ciudad'] = "❌No se aceptan números en la ciudad"

    if precio_min and not precio_min.isdigit():
        errores['precio_min'] = "❌El precio mínimo debe ser numérico"

    if precio_max and not precio_max.isdigit():
        errores['precio_max'] = "❌El precio máximo debe ser numérico"

    if (
        precio_min and precio_max and
        precio_min.isdigit() and precio_max.isdigit() and
        int(precio_min) > int(precio_max)
    ):
        errores['precio'] = "El precio mínimo no puede ser mayor al máximo"

    # FILTROS
    if not errores:
        if ciudad:
            propiedades = propiedades.filter(ciudad__icontains=ciudad)
        if tipo:
            propiedades = propiedades.filter(tipo=tipo)
        if precio_min:
            propiedades = propiedades.filter(precio__gte=int(precio_min))
        if precio_max:
            propiedades = propiedades.filter(precio__lte=int(precio_max))

    context = {
        'ciudad': ciudad,
        'tipo': tipo,
        'precio_min': precio_min,
        'precio_max': precio_max,
        'propiedades': propiedades,
        'errores': errores
    }

    return render(request, 'propiedades/propiedades.html', context)


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

     