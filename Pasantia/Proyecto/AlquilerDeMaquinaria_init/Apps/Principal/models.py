from django.db import models
#PaulaVasquez
#tabla en bd = clases en python
#--------------------CLIENTES
class Cliente(models.Model):
    uid = models.AutoField(primary_key = True) #Llave Primaria y Autoincrementada
    nombre = models.CharField(max_length = 50) #Caracter hasta 50 
    apellido = models.CharField(max_length = 50) #Caracter hasta 50
    email = models.EmailField(max_length = 200)
    telefono = models.CharField(max_length = 15)
    direccion = models.CharField(max_length = 200)

    def __str__(self):
       return self.nombre #NombreIngresado

#---------------------MAQUINAS
class Maquina(models.Model):
    uid_maquina = models.AutoField(primary_key = True) #Llave Primaria
    nombre_maquina = models.CharField(max_length = 50) 
    modelo_maquina = models.CharField(max_length = 15)
    fuente_energia = models.CharField(max_length = 50)
    estado_maquina = models.BooleanField('Maquina Activa / Maquina no Activa',default=True)

    def __str__(self):
        return self.nombre_maquina #NombreIngresado

#----------------------ALQUILERES
class Alquiler(models.Model):
    uid_alquiler = models.AutoField(primary_key = True) #Llave Primaria
    #maquina = models.ForeignKey(Maquina,null=False,blank=False,on_delete=models.CASCADE) #se elimina la renta con que no exista la maquina
    #cliente = models.ForeignKey(Cliente,null=False,blank=False,on_delete=models.CASCADE) #llave para cliente que no acepta nulo ni campo vacio
    monto_alquiler = models.DecimalField(max_digits=200, decimal_places=2, default= '0.00')

    def __str__(self):
       return self.uid_alquiler #IdIngresado
    

