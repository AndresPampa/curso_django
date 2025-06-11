from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos


# Register your models here.
#Esto lo hacemos para que nos aparezca en el panel de administracion
admin.site.register(Clientes)
admin.site.register(Articulos)
admin.site.register(Pedidos)