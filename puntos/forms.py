from django import forms
from puntos.models import Person, RolProfesional

class PersonForm(forms.ModelForm)
    class Meta:
        model = Person

        #instancia para crear listas llamando al ModelForm
        fields= [
            'name_person'
            'description_service'
            'rol_profesionals'
        ]

        #Etiquetas para pintar el formulario
        labels = {
            'name_person': 'Nompre de Persona'
            'description_service': 'Descripcion de servicio'
            'rol_profesionals': 'Rol del profesional'
        }

        #Etiquetas tipo html
        widgets = {
            'name_person': forms.TextInput(attrs={'class':'form-control'}),
            'description_service': forms.TextInput(attrs={'class':'form-control'}),
            'rol_profesionals': forms.Select(attrs={'class': 'form-control'}),

        }
