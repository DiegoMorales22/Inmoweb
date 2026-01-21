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

class MensajeContacto(models.Model):
    # Relación: muchos mensajes pueden pertenecer a una sola propiedad
    propiedad = models.ForeignKey(
        'Propiedad',                 # Modelo relacionado
        on_delete=models.CASCADE,    # Si se borra la propiedad, se borran sus mensajes
        related_name='mensajes'      # propiedad.mensajes.all()
    )

    # Datos del usuario que escribe
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()

    # Fecha automática de creación
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Cómo se verá el mensaje en el admin
        return f"Mensaje de {self.nombre} - {self.propiedad}"

class ImagenPropiedad(models.Model):
    #cada img pertenece a una solo propiedad
    propiedad = models.ForeignKey(
        Propiedad,on_delete=models.CASCADE ,related_name='imagenes'
    )
    #Guarda la imagen dentro de la carpeta propiedades/ que está dentro de la carpeta MEDIA_ROOT”.
    imagen= models.ImageField(upload_to="propiedades/")
    
    # Permite definir el orden de visualización de las imágenes
    orden = models.PositiveIntegerField(default=0)
    
    #la fecha se crea automaticamente.Fecha y hora en que se sube la imagen
    fecha= models.DateTimeField(auto_now_add=True)
    
    #activo=True → la imagen se muestra, activo=False → la imagen se oculta
    activo = models.BooleanField(default=True)

    def __str__(self):
        estado = "Activa" if self.activo else "Oculta"
        return f"Imagen de {self.propiedad.titulo} ({estado})"