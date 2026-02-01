from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .permissions import es_admin #importo mi archivo permissions.py 


from .models import Propiedad, Agente, MensajeContacto
from .forms import RegistrarPropiedad, FiltroPropiedadesForm, FormDeContacto
from django.contrib.auth.decorators import user_passes_test
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

@login_required #verifica si ul usuario esta logueado
@user_passes_test(es_admin) #el usuario cumple la condicion que expuse
def editar_propiedad(request,id):
    propiedad=get_object_or_404(Propiedad, id=id) #traeme la propiedad que tenga ese id y si no existe muestrame un error 404
    if request.method=='POST':
          form = RegistrarPropiedad(request.POST,request.FILES,instance=propiedad) #muestro el form con sus datos que envio
          if form.is_valid():
               form.save()
               return redirect('propiedades')
    else:
         form=RegistrarPropiedad(instance=propiedad)#muestro el form con los datos actuales
    return render(request,'propiedades/editar_propiedad.html', {'form': form, 'propiedad': propiedad})

@login_required #verifica si ul usuario esta logueado
@user_passes_test(es_admin) #el usuario cumple la condicion que expuse 
def eliminar_propiedad(request, id):
    propiedad = get_object_or_404(Propiedad, id=id)

    if request.method == "POST":
        propiedad.delete()
        return redirect('propiedades')

    return render(request, 'propiedades/confirmar_eliminacion.html', {
        'propiedad': propiedad
    })

def detalle_propiedad(request,id):
    propiedad= get_object_or_404(Propiedad,id=id) #aqui le digo que me busque la propiedad con ese id y si no existe devuelva un error 404
    if request.method=="POST":
        form=FormDeContacto(request.POST)# muestro el formulario con los datos que envio
        if form.is_valid():
            datos = form.cleaned_data
            # Creamos el mensaje en la base de datos
            MensajeContacto.objects.create(
                nombre=datos["nombre"],
                email=datos["email"],
                mensaje=datos["mensaje"],
                propiedad=propiedad  # relación directa
            )

            return render(request,'propiedades/registroexitoso.html',{"propiedad": propiedad})
    else:
        form = FormDeContacto()
    return render(request,"propiedades/detalle_propiedad.html", {
        "propiedad": propiedad,
        "form": form
    })          
