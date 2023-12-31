from django.db import models

# Create your models here.

class Estudiante (models.Model):
    nombre = models.CharField(max_length=60)
    apellido =models.CharField(max_length=60)
    email = models.EmailField()

class Profesor (models.Model):
    nombre = models.CharField(max_length=60)
    apellido =models.CharField(max_length=60)
    email = models.EmailField()
    profesion = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    
class Curso (models.Model):
    nombre = models.CharField(max_length=60)
    comision = models.IntegerField()
    
class Entregable(models.Model):
    nombre = models.CharField (max_length=60)
    fechaEntrega = models.DateField()
    entrega = models.BooleanField()