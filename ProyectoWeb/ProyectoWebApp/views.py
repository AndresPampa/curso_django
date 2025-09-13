from django.shortcuts import render
from django.http import HttpResponse
from carro.carro import Carro



# Create your views here.

#Tengo que crear tantas vistas como paginas tenga el proyecto

def home(request):

    carro = Carro(request)

    return render(request, 'ProyectoWebApp/home.html')



