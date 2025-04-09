from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'descripcion', 'ingredientes', 'pasos', 'tiempo_preparacion', 'imagen']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 2}),
            'ingredientes': forms.Textarea(attrs={'rows': 3}),
            'pasos': forms.Textarea(attrs={'rows': 4}),
        }
