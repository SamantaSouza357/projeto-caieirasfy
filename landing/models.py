from django.db import models

# Create your models here.

class Musica(models.Model):
    nomeMusica= models.CharField(
        max_length=255,
        verbose_name='nomeMusica'
    )
    artista= models.CharField(
        max_length=255,
        verbose_name='artista'
    )
    genero= models.CharField(
        max_length=255,
        verbose_name='genero'
    )
    link= models.CharField(
        max_length=255,
        verbose_name='link'
    )
