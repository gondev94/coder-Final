from django.urls import path
from . import views

app_name = 'traslados'

urlpatterns = [
    path('', views.index, name='index'),
    path('categoria/list/', views.categoria_list, name='categoria_list'),               #CATEGORIA LIST/CREATE/UPDATE/DETAIL/DELETE
    path('categoria/create/', views.categoria_create, name='categoria_create'),
    path('categoria/update/<int:pk>/', views.categoria_update, name='categoria_update'),
    path('categoria/detail/<int:pk>/', views.categoria_detail, name='categoria_detail'),
    path('categoria/delete/<int:pk>/', views.categoria_delete, name='categoria_delete'),
    path('cliente/list/', views.cliente_list, name='cliente_list'),                     #CLIENTE LIST/CREATE/UPDATE/DETAIL/DELETE
    path('cliente/create/', views.cliente_create, name='cliente_create'),
    path('cliente/update/<int:pk>/', views.cliente_update, name='cliente_update'),
    path('cliente/detail/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('cliente/delete/<int:pk>/', views.cliente_delete, name='cliente_delete'),
    path('flete/list/', views.flete_list, name='flete_list'),                           #FLETE LIST/CREATE/UPDATE/DETAIL/DELETE
    path('flete/create/', views.flete_create, name='flete_create'),
    path('flete/update/<int:pk>/', views.flete_update, name='flete_update'),
    path('flete/detail/<int:pk>/', views.flete_detail, name='flete_detail'),
    path('flete/delete/<int:pk>/', views.flete_delete, name='flete_delete'),    
    path('cotizacion/list/', views.cotizacion_list, name='cotizacion_list'),              #COTIZACION LIST/CREATE/UPDATE/DETAIL/DELETE
    path('cotizacion/create/', views.cotizacion_create, name='cotizacion_create'),
    path('cotizacion/update/<int:pk>/', views.cotizacion_update, name='cotizacion_update'),
    path('cotizacion/detail/<int:pk>/', views.cotizacion_detail, name='cotizacion_detail'),
    path('cotizacion/delete/<int:pk>/', views.cotizacion_delete, name='cotizacion_delete'),
    path('paquete/list/', views.paquete_list, name='paquete_list'),                        #PAQUETE LIST/CREATE/UPDATE/DETAIL/DELETE
    path('paquete/create/', views.paquete_create, name='paquete_create'),
    path('paquete/update/<int:pk>/', views.paquete_update, name='paquete_update'),
    path('paquete/detail/<int:pk>/', views.paquete_detail, name='paquete_detail'),
    path('paquete/delete/<int:pk>/', views.paquete_delete, name='paquete_delete'),
    path('transportista/list/', views.transportista_list, name='transportista_list'),           #TRANSPORTISTA LIST/CREATE/UPDATE/DETAIL/DELETE
    path('transportista/create/', views.transportista_create, name='transportista_create'),
    path('transportista/update/<int:pk>/', views.transportista_update, name='transportista_update'),
    path('transportista/detail/<int:pk>/', views.transportista_detail, name='transportista_detail'),
    path('transportista/delete/<int:pk>/', views.transportista_delete, name='transportista_delete'),
    
]