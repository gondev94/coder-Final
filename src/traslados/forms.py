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

class PaqueteForm(forms.ModelForm):
    class Meta:
        model = models.Paquete
        fields = ['nombre', 'descripcion', 'distancia', 'categoria']
    
    def clean_nombre(self):
        nombre:str = self.cleaned_data.get('nombre','')
        if len(nombre) < 3:
            raise forms.ValidationError('Debe tener al menos 3 caracteres')
        if not nombre.isalpha():
            raise forms.ValidationError('Debe contener caracteres alfabéticos')
        return nombre
    
class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ['nombre', 'apellido', 'direccion', 'telefono', 'email', 'paquete']
    
    def clean_nombre(self):
        nombre:str = self.cleaned_data.get('nombre','')
        if len(nombre) < 3:
            raise forms.ValidationError('Debe tener al menos 3 caracteres')
        if not nombre.isalpha():
            raise forms.ValidationError('Debe contener caracteres alfabéticos')
        return nombre
    
class CotizacionForm(forms.ModelForm):
    class Meta:
        model = models.Cotizacion
        fields = ['cliente', 'descripcion', 'precio_por_km', 'paquete', 'fecha_de_entrega']
    
    def clean_descripcion(self):
        descripcion:str = self.cleaned_data.get('descripcion','')
        if len(descripcion) < 3:
            raise forms.ValidationError('Debe tener al menos 3 caracteres')
        return descripcion
    
class FleteForm(forms.ModelForm):
    class Meta:
        model = models.Flete
        fields = ['cliente']
    
    def clean_cliente(self):
        cliente:str = self.cleaned_data.get('cliente','')
        if len(cliente) < 3:
            raise forms.ValidationError('Debe tener al menos 3 caracteres')
        return cliente
    
class TransportistaForm(forms.ModelForm):
    class Meta:
        model = models.Transportista
        fields = ['nombre', 'apellido', 'licencia', 'telefono', 'email', 'flete']
    
    def clean_nombre(self):
        nombre:str = self.cleaned_data.get('nombre','')
        if len(nombre) < 3:
            raise forms.ValidationError('Debe tener al menos 3 caracteres')
        if not nombre.isalpha():
            raise forms.ValidationError('Debe contener caracteres alfabéticos')
        return nombre

