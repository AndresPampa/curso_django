from django.db import models

# Create your models here.
# Creamos una clase por cada tabla de la base de datos

class Clientes(models.Model):
    #Creamos los campos que tendra la tabla
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)


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


