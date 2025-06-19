from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import *
from django.conf import settings  # Para acceder a las configuraciones del proyecto
from django.core.mail import send_mail
from gestionPedidos.forms import FormularioContacto

# Create your views here.

def busqueda_productos(request):
    return render(request, 'busqueda_productos.html')


def buscar(request):

    if request.GET['prd']:
        # mensaje = f'Articulo buscado: {request.GET['prd']}' #prd corresponde al nombre del input en el formulario
        producto = request.GET['prd']

        #Limitar los caracteres a buscar
        if len(producto) > 20:
            mensaje = 'Texto de busqueda demasiado largo'
        else:
            articulos = Articulos.objects.filter(nombre__icontains=producto)  # Filtra los artículos que contienen el texto buscado. icontains = like de sql
            return render(request, 'resultados_busqueda.html', {'articulos': articulos, 'query': producto})
    
    else:
        mensaje = 'No has introducido nada en el buscador'
    
    return HttpResponse(mensaje)


# def contacto(request):
#     if request.method == 'POST':
#         subject = request.POST['asunto']
#         message = request.POST['mensaje'] + request.POST['email']
#         #Email no de donde viene. NO confundir con el email que nos envia el usuario
#         email_from = settings.EMAIL_HOST_USER
#         #todas las direcciones de correo a las que se enviara el mensaje
#         recipient_list = ["mail@mail.com"]
#         send_mail(subject, message, email_from, recipient_list)
#         return render(request, 'gracias.html')
#     return render(request, 'contacto.html')

def contacto(request):

    if request.method == 'POST':

        mi_formulario = FormularioContacto(request.POST)
        if mi_formulario.is_valid():

            # asunto = mi_formulario.cleaned_data['']
            # email = mi_formulario.cleaned_data['']
            # mensaje = mi_formulario.cleaned_data[''] 
            #Toda la info
            informacion = mi_formulario.cleaned_data

            send_mail(
                informacion['asunto'],
                informacion['mensaje'],
                informacion.get('email', settings.EMAIL_HOST_USER),  # Usar el email del formulario o el configurado en settings
                ["tuvieja@mail.com"], #Direccion de correo a la que se enviara el mensaje
            )

            return render(request, 'gracias.html')
        
    else:

        mi_formulario = FormularioContacto() #Construye el formulario vacio
        #Ahora hay que decirle a django que contruya un html con la informacion del formulario
    
    return render(request, 'formulario_contacto.html', {'form': mi_formulario}) #le tenemos que decir que renderice el formulario en el html



def bienvenida(request):
    return render(request, 'bienvenida.html')

