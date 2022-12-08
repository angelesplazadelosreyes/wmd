from django.urls import path
from Public import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
]