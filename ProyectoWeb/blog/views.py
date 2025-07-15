from django.shortcuts import render
from blog.models import Post, Categoria  # Importamos los modelos que están dentro de la app blog

# Create your views here.

def blog(request):
    posts = Post.objects.all()  # Obtenemos todos los posts que hayamos creado
    return render(request, 'blog/blog.html', {'posts': posts})

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id) #Filtramos la categoria por su id
    posts = Post.objects.filter(categoria=categoria) #Nos filtra en base a la categoria
    return render(request, 'blog/categorias.html', {'categoria': categoria, 'posts': posts})