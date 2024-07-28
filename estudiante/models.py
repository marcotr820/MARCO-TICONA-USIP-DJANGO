from django.db import models
from . validators import validar_mayor_5, validar_solo_letras

class Curso(models.Model):
   nombre = models.CharField(max_length=50, unique=True, validators=[validar_mayor_5, validar_solo_letras])

class Profesor(models.Model):
   nombre = models.CharField(max_length=50, unique=True)
   especialidad = models.TextField()

class Estudiante(models.Model):
   nombre = models.CharField(max_length=30)
   apellido = models.CharField(max_length=30)
   curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Asignatura(models.Model):
   nombre = models.CharField(max_length=30)
   profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
   curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)


# Create your models here.
