from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('about_us/', views.about, name='about_us'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('register/', views.CustomRegisterView.as_view(), name='register'),
    path('profile/', views.UpdateProfileView.as_view(), name='profile'),
]
