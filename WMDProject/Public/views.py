from django.shortcuts import render, HttpResponse

def inicio(request):
    
    return render(request,'Public/inicio.html')