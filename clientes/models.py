
from django.db import models
from propiedades.models import Propiedad


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50,blank=True, null=True)
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to="clientes/",null=True, blank=True)
    ciudad = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.nombre}'
    
class Interes(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    propiedad = models.ForeignKey(Propiedad,on_delete=models.CASCADE)
    fecha_contacto= models.DateTimeField(auto_now_add=True)
    mensaje = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.cliente}-{self.propiedad}'
    
