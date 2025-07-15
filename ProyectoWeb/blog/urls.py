from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'), #apunta a la raiz
    path('categorias/<categoria_id>/', views.categoria, name="categoria")#me lo reconoce como parametro<>
]
