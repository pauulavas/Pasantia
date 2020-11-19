from django import forms
from .models import *

#Clientes
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__' #para todos los campos

#Maquina
class MaquinaForm(forms.ModelForm):
    class Meta:
        model = Maquina
        fields = '__all__' #para todos los campos

#Alquiler
class AlquilerForm(forms.ModelForm):
    class Meta:
        model = Alquiler
        fields = '__all__' #para todos los campos

