from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required


from .models import Propiedad, Agente
from .forms import RegistrarPropiedad, FiltroPropiedadesForm, FormDeContacto

# Create your views here.

def lista_propiedades(request):
    # 1️ Query base (todas las propiedades)
    propiedades = Propiedad.objects.all()

    # 2️ Creo el formulario con datos GET
    form = FiltroPropiedadesForm(request.GET or None)# or None evita que Django valide un formulario que nadie ha enviado.

    # 3️ Valido el formulario
    if form.is_valid():
        datos = form.cleaned_data #cleaned_data  diccionario con los datos del form

        ciudad = datos.get("ciudad")
        tipo = datos.get("tipo")
        precio_min = datos.get("precio_min")
        precio_max = datos.get("precio_max")

        # 4️ Aplico filtros SOLO si el usuario los envió

        if ciudad:
            propiedades = propiedades.filter(ciudad__icontains=ciudad)

        if tipo:
            propiedades = propiedades.filter(tipo=tipo)

        if precio_min is not None:
            propiedades = propiedades.filter(precio__gte=precio_min)

        if precio_max is not None:
            propiedades = propiedades.filter(precio__lte=precio_max)

    # 5️ Envío al template
    context = {
        "form": form,
        "propiedades": propiedades
    }

    return render(request, "propiedades/propiedades.html", context)



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

@staff_member_required
def editar_propiedad(request,id):
    propiedad=get_object_or_404(Propiedad, id=id) #traeme la propiedad que tenga ese id y si no existe muestrame un error 404
    if request.method=='POST':
          form = RegistrarPropiedad(request.POST,request.FILES,instance=propiedad) #muestro el form con sus datos que envio
          if form.is_valid():
               form.save()
               return redirect('lista_propiedades')
    else:
         form=RegistrarPropiedad(instance=propiedad)#muestro el form con los datos actuales
    return render(request,'propiedades/editar_propiedad.html', {'form': form, 'propiedad': propiedad})

@staff_member_required #“Antes de ejecutar esta función,verifica si el usuario es administrador.Si no lo es, no lo dejes entrar.”
def eliminar_propiedad(request,id):
     propiedad = get_object_or_404(Propiedad, id=id)
     propiedad.delete()
     return redirect('lista_propiedades')

def detalle_propiedad(request,id):
    propiedad= get_object_or_404(Propiedad,id=id) #aqui le digo que me busque la propiedad con ese id y si no existe devuelva un error 404
    if request.method=="POST":
        form=FormDeContacto(request.POST)# muestro el formulario con los datos que envio
        if form.is_valid():
            datos = form.cleaned_data
            nombre = datos["nombre"]
            email = datos["email"]
            mensaje=datos["mensaje"]
            context={
                "nombre":nombre,
                "email":email,
                "mensaje":mensaje,
                "propiedad":propiedad
            }
            return render(request,'propiedades/registroexitoso.html', context)
    else:
        form = FormDeContacto()
    return render(request,"propiedades/detalle_propiedad.html", {
        "propiedad": propiedad,
        "form": form
    })
        
         
