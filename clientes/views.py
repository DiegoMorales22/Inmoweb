from .models import Cliente
from django.http import HttpResponse
from django.shortcuts import render, redirect  # render muestra la página / redirect redirige después de guardar
from .forms import ClienteForm  # Importamos el formulario que creaste

# Creamos una función llamada registrar_cliente

def registrar_cliente(request):
     # Si el usuario está enviando el formulario (o sea, presionó el botón "Enviar")
    if request.method == 'POST':
        form = ClienteForm(request.POST)  # Creamos el formulario con los datos que el usuario escribió
        if form.is_valid():  # Verificamos que los datos sean correctos (por ejemplo, que el email sea válido)
            form.save()  # Guardamos los datos en la base de datos
            return redirect('registro_exitoso')  # Después de guardar, lo enviamos a una página de éxito
    else:
        # Si solo está viendo la página (no ha enviado nada)
        form = ClienteForm()  # Mostramos el formulario vacío
    
    # Le decimos a Django que muestre la plantilla y le enviamos el formulario
    return render(request,'clientes/registro_cliente.html',{"form":form})
def registro_exitoso(request):
    return render(request, 'clientes/registro_exitoso.html') 