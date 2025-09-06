from django.urls import path
from . import views

# Namespace para diferenciar las urls de las apps
app_name = "carro"

urlpatterns = [
    path('agregar/<int:producto_id>', views.agregar_producto, name='agregar'), #Pasamos el id del producto que vamos a agregar
    path('eliminar/<int:producto_id>', views.eliminar_producto, name='eliminar'),
    path('restar/<int:producto_id>', views.restar_producto, name='restar'),
    path('limpiar/', views.limpiar_carro, name='limpiar'),

]
