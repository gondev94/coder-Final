from django.urls import path
from . import views

app_name = 'traslados'

urlpatterns = [
    path('', views.index, name='index'),
    path('categoria/list/', views.categoria_list, name='categoria_list'),
    path('categoria/create/', views.categoria_create, name='categoria_create'),
    path('categoria/update/<int:pk>/', views.categoria_update, name='categoria_update'),
    path('categoria/detail/<int:pk>/', views.categoria_detail, name='categoria_detail'),
    path('cliente/list/', views.cliente_list, name='cliente_list'),
    path('cliente/create/', views.cliente_create, name='cliente_create'),
    path('cliente/update/<int:pk>/', views.cliente_update, name='cliente_update'),
    path('flete/list/', views.flete_list, name='flete_list'),
    path('flete/create/', views.flete_create, name='flete_create'),
    path('flete/update/<int:pk>/', views.flete_update, name='flete_update'),
    path('cotizacion/list/', views.cotizacion_list, name='cotizacion_list'),
    path('cotizacion/create/', views.cotizacion_create, name='cotizacion_create'),
    path('cotizacion/update/<int:pk>/', views.cotizacion_update, name='cotizacion_update'),
    path('paquete/list/', views.paquete_list, name='paquete_list'),
    path('paquete/create/', views.paquete_create, name='paquete_create'),
    path('paquete/update/<int:pk>/', views.paquete_update, name='paquete_update'),
    path('transportista/list/', views.transportista_list, name='transportista_list'),
    path('transportista/create/', views.transportista_create, name='transportista_create'),
    path('transportista/update/<int:pk>/', views.transportista_update, name='transportista_update'),
    
]