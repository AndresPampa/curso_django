# from django.shortcuts import render
from django.shortcuts import redirect
from .carro import Carro
from tienda.models import Producto
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

# Create your views here.
def agregar_producto(request: HttpRequest, producto_id: str) -> HttpResponseRedirect:
    
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)

    carro.agregar(producto) #agregamos el prodcuto al carro

    return redirect("tienda")

def eliminar_producto(request:HttpRequest, producto_id: str) -> HttpResponseRedirect:
    
    carro = Carro(request)
    proucto = Producto.objects.get(id=producto_id)

    carro.eliminar(proucto) #Eliminar

    return redirect("tienda")


def restar_producto(request: HttpRequest, producto_id: str) -> HttpResponseRedirect:
    
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)

    carro.restar_producto(producto) #Restar

    return redirect("tienda")

def limpiar_carro(request:HttpRequest) -> HttpResponseRedirect:

    carro = Carro(request)

    carro.limpiar_carro() #Limpiar el carro

    return redirect("tienda")