"""
URL configuration for ProyectoWeb project.

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicios/', include('servicios.urls')), #Agregamos los urls de la app de servicios
    path('', include('ProyectoWebApp.urls')), #Dejamos vacia la raiz para que se cargue la app por defecto
    path('blog/', include('blog.urls')), #Incluimos las urls de la app blog
    path('contacto/', include('contacto.urls')), #incluir las urls de la app contacto

]
