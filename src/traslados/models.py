from django.db import models
from datetime import datetime



class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.nombre}'
    
    class Meta:
        unique_together = ('nombre', 'descripcion')
        verbose_name = 'Categoria de Paquete'
        verbose_name_plural = 'Categorias de Paquetes'

  

class Paquete(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    distancia = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.nombre} - {self.descripcion} - {self.categoria} '
    
    class Meta:
        verbose_name = 'Paquete'
        verbose_name_plural = 'Paquetes'
        
class Cliente(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.EmailField()
    paquete = models.ForeignKey(Paquete, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nombre} - {self.direccion} - {self.telefono} - {self.email}'
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
class Cotizacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField()
    precio_por_km = models.IntegerField(default=1400)
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, editable=False)
    fecha_de_entrega = models.DateField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.total = self.paquete.distancia * self.precio_por_km
        super(Cotizacion, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.cliente} - Total: ${self.total} - Fecha de entrega: {self.fecha_de_entrega}'  
    class Meta:
        verbose_name = 'Cotizacion'
        verbose_name_plural = 'Cotizaciones'   
        

class Transportista(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    licencia = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.EmailField()


    def __str__(self):
        return f'{self.nombre} - {self.apellido}  - {self.licencia} - {self.telefono} - {self.email}'
    
    class Meta:
        verbose_name = 'Transportista'
        verbose_name_plural = 'Transportistas'
    
class Flete(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.SET_NULL, null=True)
    transportista = models.ForeignKey(Transportista, on_delete=models.SET_NULL, null=True)
    
        
    def __str__(self):
        return f'{self.cliente}'
    
    class Meta:
        verbose_name = 'Flete'
        verbose_name_plural = 'Fletes'