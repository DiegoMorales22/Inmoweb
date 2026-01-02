from .models import Propiedad #🔹 Importo mi modelo Propiedad
from django import forms #🔹 Importo las herramientas de formularios
class RegistrarPropiedad(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields=["ciudad","tipo","titulo","precio","foto_propiedad"]#elijo que campos de mi modelo mostrar
        labels={# le cambio el nombre a esos campos
            "foto_propiedad":"Sube una imagen"
        }
        widgets = { #personalizo los inputs
        "tipo": forms.Select(attrs={"class": "form-select form-control"}),#como tengo choises en mi modelos uso slect xq ya tengo ese menu de palabras a escojer 
        "titulo": forms.TextInput(attrs={"placeholder": "Ej: Casa campestre en Tunja","class": "form-control"}),
        "precio": forms.NumberInput(attrs={"min": 0, "class": "form-control"})#uso Bootstrap para estilisar
        }

class FiltroPropiedadesForm(forms.Form): #“La clase FiltroPropiedadesForm hereda de forms.Form”.
    ciudad = forms.CharField(
        required=False,
        max_length=50
    )
    

    tipo = forms.ChoiceField( #🔹 Menú desplegable
        required=False, # 🔹 No es Obligatorio
        choices=[('', 'Todos los tipos')] + Propiedad.TIPO_CHOICES # uso los choices del modelo
    )

    precio_min = forms.IntegerField( #🔹 Solo Numeros
        required=False,
        min_value=0 #🔹 No negativos
    )
    precio_max = forms.IntegerField(
        required=False,
        min_value=0
    )
    def clean_ciudad(self):
        ciudad = self.cleaned_data.get("ciudad") #🔹 Obtengo el valor limpio self es el formulario que el usuario envio, cleaned_data = diccionario que Django crea automaticamente “Dame el valor del campo ciudad si existe”,  “Formulario, dame lo que el usuario escribió en el campo ciudad,pero solo si ya pasó la validación”
       
        
        if ciudad and not ciudad.isalpha():#🔹 si escribio algo aparte de Texto
            raise forms.ValidationError(
                "La ciudad solo puede contener letras"
            )
        return ciudad
    def clean(self):#metodo usado por el hijo para 2 campos
        datos = super().clean() # “Dame el resultado de todo lo que ya validaste” es pedirle al padre lo que yá Valido

        precio_min = datos.get("precio_min")
        precio_max = datos.get("precio_max")

        if precio_min is not None and precio_max is not None: #solo pregunto si los dos datos campos existen o se llenaron en mi form 
            if precio_min > precio_max:
                raise forms.ValidationError(#lansame un error
                    "El precio mínimo no puede ser mayor que el precio máximo."
                )

        return datos


        




