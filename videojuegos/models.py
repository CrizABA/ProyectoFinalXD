from django.db import models

# Create your models here.
from django.db import models

class VideoJuego(models.Model):
    nombre = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    fechalanzamiento = models.DateField()
    plataforma = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
