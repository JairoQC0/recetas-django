
# Create your models here.
from django.db import models

class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    pasos = models.TextField()
    tiempo_preparacion = models.IntegerField(help_text="Minutos")
    imagen = models.ImageField(upload_to='recetas/', null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
