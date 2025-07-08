from django.contrib import admin
from .models import Servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


#Registramos nuestro modelo Servicio en el panel de administración de Django
admin.site.register(Servicio, ServicioAdmin) #tenemos que agregar la clase ServicioAdmin para que se muestre

