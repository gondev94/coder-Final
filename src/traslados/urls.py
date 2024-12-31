from django.urls import path
from . import views

app_name = 'traslados'

urlpatterns = [
    path('', views.index, name='index'),
    path('categoria/list/', views.categoria_list, name='categoria_list'),
    path('categoria/create/', views.categoria_create, name='categoria_create'),
    path('cliente/list/', views.cliente_list, name='cliente_list'),
    path('flete/list/', views.flete_list, name='flete_list'),
    path('cotizacion/list/', views.cotizacion_list, name='cotizacion_list'),
    path('paquete/list/', views.paquete_list, name='paquete_list'),
    path('transportista/list/', views.transportista_list, name='transportista_list'),
    path('cliente/create/', views.cliente_create, name='cliente_create'),
    path('flete/create/', views.flete_create, name='flete_create'),
    path('cotizacion/create/', views.cotizacion_create, name='cotizacion_create'),
    path('paquete/create/', views.paquete_create, name='paquete_create'),
    path('transportista/create/', views.transportista_create, name='transportista_create'),
    
]