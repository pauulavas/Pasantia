from django.shortcuts import render,redirect
#cliente
from .models import Cliente
from .forms import ClienteForm
#maquina
from .models import Maquina
from .forms import MaquinaForm
#alquiler
from .models import Alquiler
from .forms import AlquilerForm

#def inicio(request):
    #return render(request,'index.html')


#---------------------------------CLIENTES

def inicio(request):
    clientes = Cliente.objects.all()      #Lista clientes
    return render(request,'index.html',{'clientes':clientes})
    


#Crear Cliente
def crearCliente(request):
    if request.method == 'GET':
        form = ClienteForm()
        contexto = {
            'form':form
        }
    else:
        form = ClienteForm(request.POST)
        contexto = {
            'form':form
        }
        #print(form)
        if form.is_valid():
            form.save()
            return redirect('index') #redireccionar y guarda valores
    return render(request,'CrearCliente.html',contexto)


#Editar Cliente
def editarCliente(request,id):
    cliente = Cliente.objects.get(uid = id) #el id sea igual al que se ha guardado en uid
    if request.method == 'GET':
        form = ClienteForm(instance = cliente) #cliente del id
        contexto ={
            'form': form
        }
    else:
        form = ClienteForm(request.POST, instance = cliente)
        contexto ={
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'CrearCliente.html',contexto)


#Eliminar Cliente
def eliminarCliente(request,id):
    cliente = Cliente.objects.get(uid = id)
    cliente.delete()
    return redirect('index')



#---------------------------------------Maquinaria
def inicioMaquina(request):
    maquina = Maquina.objects.all()      #Lista maquinarias
    return render(request,'index.html',{'maquina':maquina})


#Crear Maquina
def crearMaquina(request):
    if request.method == 'GET':
        form = MaquinaForm()
        contexto = {
            'form':form
        }
    else:
        form = MaquinaForm(request.POST)
        contexto = {
            'form':form
        }
        #print(form)
        if form.is_valid():
            form.save()
            return redirect('index') #redireccionar y guarda valores
    return render(request,'CrearMaquina.html',contexto)


#Editar Maquina
def editarMaquina(request,id):
    maquina = Maquina.objects.get(uid_maquina = id) #el id sea igual al que se ha guardado en uid
    if request.method == 'GET':
        form = MaquinaForm(instance = maquina) #maquina del id
        contexto ={
            'form': form
        }
    else:
        form = MaquinaForm(request.POST, instance = maquina)
        contexto ={
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'CrearMaquina.html',contexto)


#Eliminar Maquina
def eliminarMaquina(request,id):
    maquina = Maquina.objects.get(uid_maquina = id)
    maquina.delete()
    return redirect('index')


#---------------------------------------Alquiler
def inicioAlquiler(request):
    alquiler = Alquiler.objects.all()      #Lista alquileres
    return render(request,'index.html',{'alquiler':alquiler})


#Crear Alquiler
def crearAlquiler(request):
    if request.method == 'GET':
        form = AlquilerForm()
        contexto = {
            'form':form
        }
    else:
        form = AlquilerForm(request.POST)
        contexto = {
            'form':form
        }
        #print(form)
        if form.is_valid():
            form.save()
            return redirect('index') #redireccionar y guarda valores
    return render(request,'CrearAlquiler.html',contexto)


#Editar Alquiler
def editarAlquiler(request,id):
    alquiler = Alquiler.objects.get(uid_alquiler = id) #el id sea igual al que se ha guardado en uid
    if request.method == 'GET':
        form = AlquilerForm(instance = alquiler) #alquiler del id
        contexto ={
            'form': form
        }
    else:
        form = AlquilerForm(request.POST, instance = alquiler)
        contexto ={
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'CrearAlquiler.html',contexto)


#Eliminar Alquiler
def eliminarAlquiler(request,id):
    alquiler = Alquiler.objects.get(uid_alquiler = id)
    alquiler.delete()
    return redirect('index')


