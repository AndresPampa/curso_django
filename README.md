# curso_django

Curso del gallego de pildoras informaticas:
https://www.youtube.com/watch?v=7XO1AzwkPPE&list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB&index=9  


## Para empezar  
1. django-admin startproject "nombre del proyecto"  
2. py or python manage.py runserver  



## Crear app con sus bases de datos
1. python manage.py startapp "Nombre de la app" --> Crea la app  
2. python manage.py check "nombre de la app" --> para chequear si se creo bien  
3. python manage.py makemigrations -->para crear las tablas  
4. python manage.py sqlmigrate "nombre de la app" 0001 (numero que te da el paso anterior de makemigrations) --> EN consola se va a ver el codigo sql para crear las tablas  
5. python manage.py migrate --> para ejecutar el codigo sql y crear las tablas  


## Insertar datos(INSERT INTO)
python manage.py shell 

"Se abre la terminal" y dentro tenemos que escribir from "Nombre del proyecto"(gestionPedidos).models import "Base de datos(clase)"
creamos una variable a la cual le asignamos la clase y completamos en funcion de los argumentos que tenga la clase.
despues hacemos esa variable .save() y automaticamente se insertara un registro en la base de datos  

Por ejemplo:
>>> from gestionPedidos.models import Articulos  
>>> art=Articulos(nombre='mesa', seccion='decoracion', precio=90000)  
>>> art.save()

o con una unica instruccion por ejemplo:   

art3=Articulos.objects.create(nombre='taladro', seccion='ferreteria', precio=65000) 

## Actualizar un registro(UPDATE)

>>> art.precio=135000
>>> art.save()


## Eliminar un registro(DELETE)

>>> art4 = Articulos.objects.get(id=2)  
>>> art4.delete()
retorna: (1, {'gestionPedidos.Articulos': 1})

## Hacer un SELECT

>>> lista=Articulos.objects.all()
>>> lista
retorna: <QuerySet [<Articulos: Articulos object (1)>, <Articulos: Articulos object (3)>]>

En esta parte creamos el __str__() y corremos  ```python manage.py makemigrations``` y despues ```python manage.py migrate```

>>> lista.query.__str__()
retorna: 'SELECT "gestionPedidos_articulos"."id", "gestionPedidos_articulos"."nombre", "gestionPedidos_articulos"."seccion", "gestionPedidos_articulos"."precio" FROM "gestionPedidos_articulos"'

### SELECT con WHERE

Articulos.objects.filter(nombre='mesa', seccion='decoracion')

Si queresmos escribir menor que < o mayor que > debemos utilizar caracteres especiales:   
__gte= -> "grater than" y __lte= -> "lesser than"  
o hay una funcion para rangos de valores -> __range(10, 150)

Articulos.objects.filter(nombre='mesa', seccion__get=100)

### ORDER BY

Articulos.objects.filter(precio__get=50).order_by('-precio') #El signo menos es para indicar el ```DESC```


## Create Super User
----> python manage.py createsuperuser
Nombre de usuario (leave blank to use 'user Random'): 
Dirección de email: mail@mail.com
Password: **********
Password (again): **********
Superuser created successfully.

## Enviar un Mail por consola
python manage.py shell
>>> from django.core.mail import send_mail
>>> send_mail('asunto', 'mensaje', 'tuvieja@gmail.com', ['cursos@django.com.ar'], fail_silently=False)

