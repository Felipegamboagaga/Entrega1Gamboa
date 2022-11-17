from django.db import models

# Create your models here.
class familia(models.Model):
    nombre = models.CharField(max_length =50)
    edad = models.IntegerField()
  
    
    def __str__(self) -> str:
        return self.nombre

class Aficion(models.Model):
    nombre_equipo = models.CharField(max_length =50)
    campeonatos = models.IntegerField()
   
    
    def __str__(self) -> str:
        return self.nombre
    
class Experiencia(models.Model):
    Lenguaje = models.CharField(max_length =50)
    tiempo = models.IntegerField()
   
    
    def __str__(self) -> str:
        return self.nombre

