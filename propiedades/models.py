from django.db import models

# Create your models here.

class Agente(models.Model):
    nombre =models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=50, default=0)
    email = models.EmailField()
    perfil = models.ImageField(upload_to="agentes/", null=True, blank=True)
    def __str__(self):
        return f'{self.nombre}'
    
class Propiedad(models.Model):
    TIPO_CHOICES = [
    ('casa', 'Casa'),
    ('apartamento', 'Apartamento'), # respuestas validas
    ('lote', 'Lote'),
    ('oficina', 'Oficina'),
]
    titulo = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)  # 👈 Aquí usamos los choices
    descripcion = models.TextField(blank=True, null=True)
    publicada = models.BooleanField(default=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    metros_cuadrados = models.IntegerField(default=0)
    agente = models.ForeignKey(
        Agente,
        on_delete=models.CASCADE,
        related_name="propiedades",# esto le dice a django que cuando busq todas las propiedades de un agente lo busque con la palabra propiedades
        null=True,       # 👈 permite que esté vacío en la BD
        blank=True       # 👈 permite que esté vacío en formularios/admin
    )
    foto_propiedad = models.ImageField(upload_to="propiedades/", null=True, blank=True)
    def __str__(self):
        return f'{self.titulo}'


    """
    🚀 Retos para ser PRO en filters
🔹 Reto 1: Precio

Trae todas las propiedades que cuesten menos de 200 millones.
    """

#

"""
reto # 1
>>> Propiedad.objects.filter(titulo__icontains="casa")
<QuerySet [<Propiedad: Casa Blanca>, <Propiedad: Casa Campestre El Encanto>, <Propiedad: Casa Moderna San Laureano>]>
reto # 2
>>> Propiedad.objects.filter(precio__lt=200000000)
<QuerySet [<Propiedad: Apartamento La Esperanza>, <Propiedad: Cabaña Río Claro>]>
reto # 3
>>> Propiedad.objects.filter(ciudad__icontains="Tunja", precio__gt=150000000)
<QuerySet [<Propiedad: Casa Blanca>, <Propiedad: Casa Campestre El Encanto>]>
Reto # 4 
>>> Propiedad.objects.filter(Q(ciudad__icontains="tunja")|Q(ciudad__icontains="Duitama"))
<QuerySet [<Propiedad: Casa Blanca>, <Propiedad: Casa Campestre El Encanto>]>
Reto # 5
>>> Propiedad.objects.values("titulo","precio").order_by("titulo","precio")
<QuerySet [{'titulo': 'Apartamento Central en Duitama', 'precio': Decimal('250000000.00')}, {'titulo': 'Apartamento La Esperanza', 'precio': Decimal('150000000.00')}, {'titulo': 'Cabaña Río Claro', 'precio': Decimal('160000000.00')}, {'titulo': 'Casa Blanca', 'precio': Decimal('350000000.00')}, {'titulo': 'Casa Campestre El Encanto', 'precio': Decimal('320000000.00')}, {'titulo': 'Casa Moderna San Laureano', 'precio': Decimal('320000000.00')}, {'titulo': 'Finca Los Pinos', 'precio': Decimal('480000000.00')}, {'titulo': 'nombre', 'precio': Decimal('600000000.00')}]>
"""