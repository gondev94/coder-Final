from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    return render(request, 'traslados/index.html')

def categoria_list(requets):
    categorias = models.Categoria.objects.all()
    return render(requets, 'traslados/categoria_list.html', {'categorias': categorias})
