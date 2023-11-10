from django.db import models

class Cancion(models.Model):
    titulo = models.CharField(max_length=50)
    artista = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    año_lanzamiento = models.IntegerField()
    genero = models.CharField(max_length=50)
    
    def __str__(self):
        return self.titulo
