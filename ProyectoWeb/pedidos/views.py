from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Pedido, LineaPedido
from carro.carro import Carro
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Create your views here.
@login_required
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id = key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido_id=pedido
        ))
    
    LineaPedido.objects.bulk_create(lineas_pedido) #Muchos insert into como su fuera un lote

    enviar_mail(pedido=pedido, 
                lineas_pedido=lineas_pedido, 
                nombre_usuario=request.user.username, 
                email_usuario=request.user.mail)

    messages.success(request, "El pedido se ha creado correctamente")


    return redirect('/tienda') #../tienda


def enviar_mail(**kwargs):
    
    asunto = 'Gracias por el pedido'
    mensaje = render_to_string("emails/pedido.html", {
        'pedido':kwargs.get('pedido'),
        'lineas_pedido':kwargs.get('lineas_pedido'),
        'nombre_usuario':kwargs.get('nombre_usuario'),
    })

    mensaje_texto = strip_tags(mensaje)
    from_email = 'tumail@mail.com'
    # to_mail = kwargs.get('email_usuario')
    to_mail = 'mail_de_prueba@mail.com' #Mail de prueba para debuggear

    send_mail(asunto, mensaje_texto, from_email, [to_mail], html_message=mensaje)