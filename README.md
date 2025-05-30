# curso_django

Curso del gallego de pildoras informaticas:
https://www.youtube.com/watch?v=7XO1AzwkPPE&list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB&index=9  


## Para empezar  





## Crear app con sus bases de datos
1. python manage.py startapp "Nombre de la app" --> Crea la app  
2. python manage.py check "nombre de la app" --> para chequear si se creo bien  
3. python manage.py makemigrations -->para crear las tablas  
4. python manage.py sqlmigrate "nombre de la app" 0001 (numero que te da el paso anterior de makemigrations) --> EN consola se va a ver el codigo sql para crear las tablas  
5. python manage.py migrate --> para ejecutar el codigo sql y crear las tablas  
