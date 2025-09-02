from django.db import models

# Create your models here.
# Mapeo ORM (Object Relational Mapping)
class CategoriaProd(models.Model):
    nombre = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    # Meta sirve para definir el nombre en singular y plural del modelo en la administración
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField()
    categorias = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='tienda', null=True, blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.nombre