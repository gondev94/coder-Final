from django.shortcuts import render, redirect
from . import models, forms
from django.http import HttpResponse, HttpRequest


# Create your views here.
def index(request):
    return render(request, 'traslados/index.html')

def categoria_list(requets):
    categorias = models.Categoria.objects.all()
    return render(requets, 'traslados/categoria_list.html', {'categorias': categorias})

def categoria_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = form = forms.CategoriaForm()
    if request.method == 'POST':
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traslados:categoria_list')
    return render(request, 'traslados/categoria_form.html', {'form': form})

