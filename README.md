# wmd
trabajo para examen de arquitectura de software

Python 3.9.4
HTML 5

# ================================================================================================

Pasos para la creación del proyecto:

1. Crear proyecto:
	django-admin startproject WMDProject

2. Ir a la carpeta del proyecto:
	cd WMDProject

3. Crear la App:
	python manage.py startapp Public
	python manage.py startapp User

4. Probar la conexión:
	python manage.py runserver

5. Hacer vistas:
	Public -> views.py (hay 1 vista)
	User -> views.py (hay 3 vistas: cliente, restaurant y repartidor)

(5). En views importar httpResponse (para ir haciendo pruebas) y definir vistas así:
	def vista(request):
      		return HttpResponse('nombre provisorio')

6. Para cada app crear un archivo urls.py

7. (video 28)ir a archivos url de cada app e importar las urls:
	from django.urls import path
	from Public import views
    luego crear patterns:
    urlpatterns = [
    path('', views.inicio, name='Inicio'),
]

    from django.urls import path
    from User import views
	luego crear patterns
    urlpatterns = [
    path('buscarProducto/', views.buscarProducto, name='BuscarProducto'),
    path('datosCliente/', views.datosCliente, name='DatosCliente'),
    path('verPedido/', views.verPedido, name='VerPedido'),
]

8. (video 28)enlazar el urls.py del proyecto con el de la aplicación:
	en el urls.py del proyecto importar include y path 
	
    from django.contrib import admin
from django.urls import path, include

    urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Public.urls')),
    path('user/', include('User.urls')),
]

9. probar si funciona el server (ojo, hay que estar en la carpeta adecuada, si no da error)
	python manage.py runserver

10. crear dentro de la app (Public) la carpeta templates y dentro de esta la carpeta Public, en esta última se crean los html de las vistas
    crear dentro de la app (User) la carpeta templates y dentro de esta la carpeta User, en esta última se crean los html de las vistas

11. Ir a settings.py (del proyecto) e importar la app en la parte "INSTALLED_APPS"

    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Public',
    'User',
]

12. Ir a views.py de Public y reemplazar el return HttpRequest("nombre") por return render(request,'Public/inicio.html')

    Luego a los views.py de User y reemplazar el return HttpRequest("nombre") por:
    return render(request,'User/buscarProducto.html')
    return render(request,'User/datos.html')
    return render(request,'User/pedido.html')

