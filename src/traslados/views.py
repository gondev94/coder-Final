from django.shortcuts import render, redirect
from .forms import CategoriaForm, ClienteForm, CotizacionForm, FleteForm, PaqueteForm, TransportistaForm
from django.http import HttpResponse, HttpRequest
from .models import Categoria, Cliente, Flete, Cotizacion, Paquete, Transportista
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'traslados/index.html')

########################################################
@login_required
def categoria_list(requets):
    query = Categoria.objects.all()
    return render(requets, 'traslados/categoria_list.html', {'object': query})

@login_required
def categoria_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = CategoriaForm()
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traslados:categoria_list')
    return render(request, 'traslados/categoria_form.html', {'form': form})

@login_required
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

@login_required
def categoria_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Categoria.objects.get(id=pk)
    return render(request, 'traslados/categoria_detail.html', {'object': query})

@login_required
def categoria_delete (request: HttpRequest, pk: int) -> HttpResponse:
    query = Categoria.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()    
        return redirect('traslados:categoria_list')
    return render(request, 'traslados/categoria_confirm_delete.html', {'object': query})


#########################################################
@login_required
def cliente_list(requets: HttpRequest) -> HttpResponse:
    query = requets.GET.get('query')
    if query:
        query = Cliente.objects.filter(nombre__icontains=query)
    else:
        query = Cliente.objects.all()    
    return render(requets, 'traslados/cliente_list.html', {'object_list' : query})

@login_required
def cliente_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traslados:cliente_list')
    return render(request, 'traslados/cliente_form.html', {'form': form})

@login_required
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

@login_required
def cliente_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Cliente.objects.get(id=pk)
    return render(request, 'traslados/cliente_detail.html', {'cliente': query})

@login_required
def cliente_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = Cliente.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('traslados:cliente_list')
    return render(request, 'traslados/cliente_confirm_delete.html', {'cliente': query})
########################################################
@login_required
def flete_list(requets: HttpRequest) -> HttpResponse:
    query = requets.GET.get('query')
    if query:
        query = Flete.objects.filter(nombre__icontains=query)
    else:
        query = Flete.objects.all()
    return render(requets, 'traslados/flete_list.html', {'object_list' : query})

@login_required
def flete_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = FleteForm()
    if request.method == 'POST':
        form = FleteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traslados:flete_list')
    return render(request, 'traslados/flete_form.html', {'form': form})

@login_required
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

@login_required
def flete_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Flete.objects.get(id=pk)
    return render(request, 'traslados/flete_detail.html', {'flete': query})

@login_required
def flete_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = Flete.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('traslados:flete_list')
    return render(request, 'traslados/flete_confirm_delete.html', {'flete': query})

########################################################
@login_required
def cotizacion_list(requets: HttpRequest) -> HttpResponse:
    query = requets.GET.get('query')
    if query:
        query = Cotizacion.objects.filter(descripcion__icontains=query)
    else:
        query = Cotizacion.objects.all()
    return render(requets, 'traslados/cotizacion_list.html', {'object_list': query})


@login_required
def cotizacion_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = CotizacionForm()
    if request.method == 'POST':
        form = CotizacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traslados:cotizacion_list')
    return render(request, 'traslados/cotizacion_form.html', {'form': form})


@login_required
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


@login_required
def cotizacion_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Cotizacion.objects.get(id=pk)
    return render(request, 'traslados/cotizacion_detail.html', {'object': query})


@login_required
def cotizacion_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = Cotizacion.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('traslados:cotizacion_list')
    return render(request, 'traslados/cotizacion_confirm_delete.html', {'object': query})

########################################################

@login_required
def paquete_list(requets: HttpRequest) -> HttpResponse:
    query = requets.GET.get('query')
    if query:
        query = Paquete.objects.filter(nombre__icontains=query)
    else:
        query = Paquete.objects.all()    
    return render(requets, 'traslados/paquete_list.html', {'object_list': query})


@login_required
def paquete_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = PaqueteForm()
    if request.method == 'POST':
        form = PaqueteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traslados:paquete_list')
    return render(request, 'traslados/paquete_form.html', {'form': form})

@login_required
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

@login_required
def paquete_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Paquete.objects.get(id=pk)
    return render(request, 'traslados/paquete_detail.html', {'paquete': query})


@login_required
def paquete_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = Paquete.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('traslados:paquete_list')
    return render(request, 'traslados/paquete_confirm_delete.html', {'paquete': query})

@login_required
########################################################
def transportista_list(requets: HttpRequest) -> HttpResponse:
    query = requets.GET.get('query')
    if query:
        query = Transportista.objects.filter(nombre__icontains=query)
    else:
        query = Transportista.objects.all()        
    return render(requets, 'traslados/transportista_list.html', {'object_list' : query})

@login_required
def transportista_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = TransportistaForm()
    if request.method == 'POST':
        form = TransportistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traslados:transportista_list')
    return render(request, 'traslados/transportista_form.html', {'form': form})

@login_required
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

@login_required
def transportista_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Transportista.objects.get(id=pk)
    return render(request, 'traslados/transportista_detail.html', {'transportista': query})

@login_required
def transportista_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = Transportista.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('traslados:transportista_list')
    return render(request, 'traslados/transportista_confirm_delete.html', {'transportista': query})
########################################################