# Importamos la clase forms de Django
from django import forms

# Importamos el modelo Cliente para crear el formulario basado en él
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente  # Indicamos con qué modelo trabaja el formulario
        fields = ["nombre", "email", "telefono", "ciudad",]  # Campos que aparecerán en el formulario
        labels={ #cambio los nombres a los campos
            "nombre":"Nombre Completo",
            "telefono":"Numero De Contacto"
        }
        help_text={ "Muestra una ayuda o descripción debajo del campo."
            "email":"ingresa un correo valido!"
        }
        error_messages = {
            'nombre': {'required': 'Por favor escribe tu nombre.'},
        }

