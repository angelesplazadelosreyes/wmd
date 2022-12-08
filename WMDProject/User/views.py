from django.shortcuts import render, HttpResponse

def buscarProducto(request):
    
    return render(request,'User/buscarProducto.html')


def datosCliente(request):
    
    render(request,'User/datos.html')


def verPedido(request):
    
    return render(request,'User/pedido.html')
