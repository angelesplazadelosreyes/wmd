from django.urls import path
from User import views

urlpatterns = [
    path('buscarProducto/', views.buscarProducto, name='BuscarProducto'),
    path('datosCliente/', views.datosCliente, name='DatosCliente'),
    path('verPedido/', views.verPedido, name='VerPedido'),
]