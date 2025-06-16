from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import *

# Create your views here.

def busqueda_productos(request):
    return render(request, 'busqueda_productos.html')


def buscar(request):

    if request.GET['prd']:
        # mensaje = f'Articulo buscado: {request.GET['prd']}' #prd corresponde al nombre del input en el formulario
        producto = request.GET['prd']
        articulos = Articulos.objects.filter(nombre__icontains=producto)  # Filtra los artículos que contienen el texto buscado. icontains = like de sql
        return render(request, 'resultados_busqueda.html', {'articulos': articulos, 'query': producto})
    else:
        mensaje = 'No has introducido nada en el buscador'
    
    return HttpResponse(mensaje)