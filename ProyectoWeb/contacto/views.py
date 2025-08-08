from django.shortcuts import render, redirect
from .forms import FormularioContacto



# Create your views here.
def contacto(request):
    #initialize
    formulario_contacto = FormularioContacto()

    if request.method == 'POST':
        formulario_contacto = FormularioContacto(request.POST) #Cargar en nuestro formulario los datos que nos llegan del POST que llena el usuario
        if formulario_contacto.is_valid(): #Chequea si se llenaron todos los campos requeridos
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')

            return redirect('/contacto/?valido')
    
    #mensaje de success para el usuario


    return render(request, 'contacto/contacto.html', {'formulario': formulario_contacto})