from django.db import models

# Create your models here.
# Creamos una clase por cada tabla de la base de datos

class Clientes(models.Model):
    #Creamos los campos que tendra la tabla
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50, verbose_name='Apellidos')#verbose_name es para que en el panel de administracion se muestre con ese nombre
    email = models.EmailField(blank=True, null=True)#Esto es para que el campo no sea obligatorio y para pueda ser null
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return f'El nombre es: {self.nombre}, la seccion es: {self.seccion} y el precio es: ${self.precio}'


class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()


#Cada vez que modificamos algo de los modelos debemos hacer una migracion -> makemigrations + migrate
