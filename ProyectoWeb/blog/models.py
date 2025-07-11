from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#modelo para insertar categorias
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    
    def __str__(self):
        return self.nombre

#modelo para insertar blogs
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True) #Por defecto puede quedar en blanco
    autor = models.ForeignKey(User, on_delete=models.CASCADE) #relaciona con el modelo User y si eliminamos un usuario, elimina sus posts
    categoria = models.ManyToManyField(Categoria) #relaciona con el modelo Categoria, puede tener varias categorias
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    
    def __str__(self):
        return self.titulo