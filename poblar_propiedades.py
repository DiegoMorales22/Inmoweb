# Importes de librerías estándar y Django
import os                          # trabajar con rutas y variables de entorno
import django                      # necesitamos inicializar Django manualmente
from django.core.files import File # clase que envuelve un archivo para guardarlo en un FileField/ImageField

# Configurar el entorno de Django (decirle dónde están los settings)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "InmoWeb.settings")
django.setup()  # carga la configuración y registra las apps (clave para poder usar los modelos aquí)

# Importar los modelos después de hacer django.setup()
from propiedades.models import Propiedad, Agente

# Lista con los datos que queremos insertar (puedes añadir más diccionarios)
propiedades = [
    {
        "titulo": "Casa en Tunja",
        "precio": 250000000,
        "ciudad": "Tunja",
        "metros_cuadrados": 120,
        "agente": 1,  # id del agente que ya debe existir en la BD
        "imagen": r"C:\Users\Diego\imagenes\casa1.jpg"  # ruta absoluta al archivo en tu PC
    },
    {
        "titulo": "Apartamento en Bogotá",
        "precio": 350000000,
        "ciudad": "Bogotá",
        "metros_cuadrados": 80,
        "agente": 1,
        "imagen": r"C:\Users\Diego\imagenes\apto1.jpg"
    },
]

# Bucle que recorre la lista y guarda cada propiedad en la BD
for p in propiedades:
    agente = Agente.objects.get(id=p["agente"])  # busca el agente por su id en la BD
    propiedad = Propiedad(
        titulo=p["titulo"],
        precio=p["precio"],
        ciudad=p["ciudad"],
        metros_cuadrados=p["metros_cuadrados"],
        agente=agente
    )
    # Abrimos el archivo de imagen en modo binario y lo guardamos en el campo ImageField
    with open(p["imagen"], "rb") as f:
        # .save(nombre_archivo, Fileobj) copia el archivo a MEDIA_ROOT según upload_to del campo
        propiedad.foto_propiedad.save(os.path.basename(p["imagen"]), File(f))
    # Guardamos el resto de campos del modelo en la BD
    propiedad.save()
    print(f"✅ Propiedad guardada: {propiedad.titulo}")



"""
prop = Propiedad.objects.get(id=3)   # o el ID de tu propiedad
print(prop.foto_propiedad)           # te dice qué hay en la BD
print(prop.foto_propiedad.url)       # la URL que debería abrir el navegador
print(prop.foto_propiedad.path)      # la ruta completa en tu PC

"""