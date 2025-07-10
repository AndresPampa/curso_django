from django.shortcuts import render
from servicios.models import Servicio #importamos el modelo que esta dentro de la app servicios

# Create your views here.
def servicios(request):

    servicios = Servicio.objects.all() #importamos todos los servicios que hayamos construidos

    return render(request, "servicios/servicios.html", {'servicios': servicios}) #Le pasamos los servicios a la plantilla para que los cargue