from django import forms
from .models import Propiedad

class RegistrarPropiedad(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields=["ciudad","tipo","titulo","precio","foto_propiedad"]#elijo que campos de mi modelo mostrar
        labels={# le cambio el nombre a esos campos
            "foto_propiedad":"Sube una imagen"
        }
        widgets = { #personalizo los inputs
        "tipo": forms.Select(attrs={"class": "form-select form-control"}),#como tenco choises en mi modelos uso slect xq ya tengo ese menu de palabras a escojer 
        "titulo": forms.TextInput(attrs={"placeholder": "Ej: Casa campestre en Tunja","class": "form-control"}),
        "precio": forms.NumberInput(attrs={"min": 0, "class": "form-control"})#uso Bootstrap para estilisar
        }
