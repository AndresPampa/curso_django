"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project1.views import saludo
from project1.views import despedida
from project1.views import dameFecha
# Me canse
from project1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('nosvemos/', despedida),
    path('horayfecha/', dameFecha),
    # Esta es la forma de pasarle parametros a una vista
    path('edades/<int:edad>/<int:anio>', calculaEdad),
    path('cursoc/', curso_c),
    path('cursocss/', curso_css),
]
