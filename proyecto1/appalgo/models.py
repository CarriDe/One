from django.db import models

class pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    año = models.IntegerField()
    genero = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.titulo} ({self.año}) - {self.genero} - Dir: {self.director}'