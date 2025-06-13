from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos


# Register your models here.
#Esto lo hacemos para que nos aparezca en el panel de administracion

class ClientesAdmin(admin.ModelAdmin): #hereda de admin.ModelAdmin
    #agregar mas columnas al panel de administracion
    list_display = ('nombre', 'apellido', 'email', 'telefono')  # Campos a mostrar en el panel de administración
    #Buscador
    search_fields = ('nombre', 'apellido') # Campos por los que se puede buscar en el panel de administracion


class ArticulosAdmin(admin.ModelAdmin):
    #filtro
    list_filter = ('seccion',) #Agregar al final una coma ya que es una tupla


class PedidosAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fecha', 'entregado')
    list_filter = ('fecha',)
    date_hierarchy = 'fecha' #no hace falta parentesis, es para que se muestre un calendario en el panel de administracion



admin.site.register(Clientes, ClientesAdmin)#se registra tambien la clase ClientesAdmin para que se muestre en el panel de administracion
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)