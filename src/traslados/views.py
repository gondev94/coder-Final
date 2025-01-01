from django.shortcuts import render, redirect
from .forms import CategoriaForm, ClienteForm, CotizacionForm, FleteForm, PaqueteForm, TransportistaForm
from django.http import HttpResponse, HttpRequest
from .models import Categoria, Cliente, Flete, Cotizacion, Paquete, Transportista


# Create your views here.
def index(request):
    return render(request, 'traslados/index.html')

def categoria_list(requets):
    query = Categoria.objects.all()
    return render(requets, 'traslados/categoria_list.html', {'object': query})

########################################################
def categoria_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = CategoriaForm()
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traslados:categoria_list')
    return render(request, 'traslados/categoria_form.html', {'form': form})


def categoria_update(request: HttpRequest, pk: int) -> HttpResponse:
    query = Categoria.objects.get(id=pk)
    if request.method == 'GET':
        form = CategoriaForm(instance=query)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('traslados:categoria_list')
    return render(request, 'traslados/categoria_form.html', {'form': form})

def categoria_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Categoria.objects.get(id=pk)
    return render(request, 'traslados/categoria_detail.html', {'object': query})




#########################################################
def cliente_list(requets: HttpRequest) -> HttpResponse:
    query = Cliente.objects.all()
    context = {"object_list": query}
    return render(requets, 'traslados/cliente_list.html', context)

def cliente_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traslados:cliente_list')
    return render(request, 'traslados/cliente_form.html', {'form': form})

def cliente_update(request: HttpRequest, pk: int) -> HttpResponse:
    query = Cliente.objects.get(id=pk)
    if request.method == 'GET':
        form = ClienteForm(instance=query)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('traslados:cliente_list')
    return render(request, 'traslados/cliente_form.html', {'form': form})

########################################################
def flete_list(requets: HttpRequest) -> HttpResponse:
    query = Flete.objects.all()
    context = {"object_list": query}
    return render(requets, 'traslados/flete_list.html', context)

def flete_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = FleteForm()
    if request.method == 'POST':
        form = FleteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traslados:flete_list')
    return render(request, 'traslados/flete_form.html', {'form': form})

def flete_update(request: HttpRequest, pk: int) -> HttpResponse:
    query = Flete.objects.get(id=pk)
    if request.method == 'GET':
        form = FleteForm(instance=query)
    if request.method == 'POST':
        form = FleteForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('traslados:flete_list')
    return render(request, 'traslados/flete_form.html', {'form': form})

########################################################
def cotizacion_list(requets: HttpRequest) -> HttpResponse:
    query = Cotizacion.objects.all()
    context = {"object_list": query}
    return render(requets, 'traslados/cotizacion_list.html', context)

def cotizacion_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = CotizacionForm()
    if request.method == 'POST':
        form = CotizacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traslados:cotizacion_list')
    return render(request, 'traslados/cotizacion_form.html', {'form': form})

def cotizacion_update(request: HttpRequest, pk: int) -> HttpResponse:
    query = Cotizacion.objects.get(id=pk)
    if request.method == 'GET':
        form = CotizacionForm(instance=query)
    if request.method == 'POST':
        form = CotizacionForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('traslados:cotizacion_list')
    return render(request, 'traslados/cotizacion_form.html', {'form': form})

########################################################
def paquete_list(requets: HttpRequest) -> HttpResponse:
    query = Paquete.objects.all()
    context = {"object_list": query}
    
    return render(requets, 'traslados/paquete_list.html', context)



def paquete_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = PaqueteForm()
    if request.method == 'POST':
        form = PaqueteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traslados:paquete_list')
    return render(request, 'traslados/paquete_form.html', {'form': form})

def paquete_update(request: HttpRequest, pk: int) -> HttpResponse:
    query = Paquete.objects.get(id=pk)
    if request.method == 'GET':
        form = PaqueteForm(instance=query)
    if request.method == 'POST':
        form = PaqueteForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('traslados:paquete_list')
    return render(request, 'traslados/paquete_form.html', {'form': form})

########################################################
def transportista_list(requets: HttpRequest) -> HttpResponse:
    query = Transportista.objects.all()
    context = {"object_list": query}
    
    return render(requets, 'traslados/transportista_list.html', context)

def transportista_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = TransportistaForm()
    if request.method == 'POST':
        form = TransportistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traslados:transportista_list')
    return render(request, 'traslados/transportista_form.html', {'form': form})

def transportista_update(request: HttpRequest, pk: int) -> HttpResponse:
    query = Transportista.objects.get(id=pk)
    if request.method == 'GET':
        form = TransportistaForm(instance=query)
    if request.method == 'POST':
        form = TransportistaForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('traslados:transportista_list')
    return render(request, 'traslados/transportista_form.html', {'form': form})
########################################################