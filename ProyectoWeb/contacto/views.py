from django.shortcuts import render
from .forms import FormularioContacto


# Create your views here.
def contacto(request):
    #initialize
    formulario_contacto = FormularioContacto()

    return render(request, 'contacto/contacto.html', {'formulario': formulario_contacto})