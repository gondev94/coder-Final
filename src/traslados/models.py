from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.nombre} - {self.descripcion}'