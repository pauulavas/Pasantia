"""AlquilerDeMaquinaria_init URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#Cliente
from Apps.Principal.views import inicio,crearCliente,editarCliente,eliminarCliente
#Maquina
from Apps.Principal.views import crearMaquina,editarMaquina,eliminarMaquina
#Alquiler
from Apps.Principal.views import crearAlquiler,editarAlquiler,eliminarAlquiler
#importando def en views
#ruta para acceder a Apps


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio,name = 'index'), #como ruta localhost
    #Cliente
    path('Crear_Cliente/',crearCliente, name = 'Crear_Cliente'), #Ruta para crear cliente
    path('Editar_Cliente/<int:id>/',editarCliente, name= 'Editar_Cliente'),#Ruta para editar cliente, ultimo dato nombre asociado a la ruta
    path('Eliminar_Cliente/<int:id>/',eliminarCliente, name= 'Eliminar_Cliente'),
    #Maquina
    path('Crear_Maquina/',crearMaquina, name = 'Crear_Maquina'), #Ruta para crear maquina 
    path('Editar_Maquina/<int:id>/',editarMaquina, name= 'Editar_Maquina'),#Ruta para editar maquina, ultimo dato nombre asociado a la ruta
    path('Eliminar_Maquina/<int:id>/',eliminarMaquina, name= 'Eliminar_Maquina'),
    #Alquiler
    path('Crear_Alquiler/',crearAlquiler, name = 'Crear_Alquiler'), #Ruta para crear alquiler
    path('Editar_Alquiler/<int:id>/',editarAlquiler, name= 'Editar_Alquiler'),#Ruta para editar alquiler, ultimo dato nombre asociado a la ruta
    path('Eliminar_Alquiler/<int:id>/',eliminarAlquiler, name= 'Eliminar_Alquiler')
]
