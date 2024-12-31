from django.urls import path
from . import views

app_name = 'traslados'

urlpatterns = [
    path('', views.index, name='index'),
    path('categoria/list', views.categoria_list, name='categoria_list'),
    path('categoria/create', views.categoria_create, name='categoria_create'),
]