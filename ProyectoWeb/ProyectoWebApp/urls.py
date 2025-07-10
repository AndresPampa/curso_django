from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('tienda', views.tienda, name='tienda'),
    path('blog', views.blog, name='blog'),
    path('contacto', views.contacto, name='contacto'),
]

#Para buscar las imágenes en la carpeta media y cualquier tipo de archivo statico
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)