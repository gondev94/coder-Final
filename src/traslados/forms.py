from django import forms
from . import models

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = ['nombre', 'descripcion']
    
    def clean_nombre(self):
        nombre:str = self.cleaned_data.get('nombre','')
        if len(nombre) < 3:
            raise forms.ValidationError('Debe tener al menos 3 caracteres')
        if not nombre.isalpha():
            raise forms.ValidationError('Debe contener caracteres alfabéticos')
        return nombre
