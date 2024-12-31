from django.shortcuts import render, redirect
from . import models, forms
from django.http import HttpResponse, HttpRequest


# Create your views here.
def index(request):
    return render(request, 'traslados/index.html')

def categoria_list(requets):
    categorias = models.Categoria.objects.all()
    return render(requets, 'traslados/categoria_list.html', {'categorias': categorias})
########################################################
def categoria_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = form = forms.CategoriaForm()
    if request.method == 'POST':
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traslados:categoria_list')
    return render(request, 'traslados/categoria_form.html', {'form': form})
#########################################################
def cliente_list(requets: HttpRequest) -> HttpResponse:
    query = models.Cliente.objects.all()
    context = {"object_list": query}
    return render(requets, 'traslados/cliente_list.html', context)

def cliente_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = forms.ClienteForm()
    if request.method == 'POST':
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traslados:cliente_list')
    return render(request, 'traslados/cliente_form.html', {'form': form})

########################################################
def flete_list(requets: HttpRequest) -> HttpResponse:
    query = models.Flete.objects.all()
    context = {"object_list": query}
    return render(requets, 'traslados/flete_list.html', context)

def flete_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = forms.FleteForm()
    if request.method == 'POST':
        form = forms.FleteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traslados:flete_list')
    return render(request, 'traslados/flete_form.html', {'form': form})

########################################################
def cotizacion_list(requets: HttpRequest) -> HttpResponse:
    query = models.Cotizacion.objects.all()
    context = {"object_list": query}
    return render(requets, 'traslados/cotizacion_list.html', context)

def cotizacion_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = forms.CotizacionForm()
    if request.method == 'POST':
        form = forms.CotizacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traslados:cotizacion_list')
    return render(request, 'traslados/cotizacion_form.html', {'form': form})

########################################################
def paquete_list(requets: HttpRequest) -> HttpResponse:
    query = models.Paquete.objects.all()
    context = {"object_list": query}
    
    return render(requets, 'traslados/paquete_list.html', context)



def paquete_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = forms.PaqueteForm()
    if request.method == 'POST':
        form = forms.PaqueteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traslados:paquete_list')
    return render(request, 'traslados/paquete_form.html', {'form': form})


########################################################
def transportista_list(requets: HttpRequest) -> HttpResponse:
    query = models.Transportista.objects.all()
    context = {"object_list": query}
    
    return render(requets, 'traslados/transportista_list.html', context)

def transportista_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = forms.TransportistaForm()
    if request.method == 'POST':
        form = forms.TransportistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traslados:transportista_list')
    return render(request, 'traslados/transportista_form.html', {'form': form})
########################################################