from django.contrib import admin

from .models import Estudiante, Curso, Profesor, Asignatura

admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Asignatura)


# Register your models here.
