from rest_framework import serializers
from . models import Curso, Profesor, Estudiante

class CursoSerializer(serializers.ModelSerializer):
   class Meta:
      model = Curso
      fields = '__all__'

class ProfesorSerializer(serializers.ModelSerializer):
   class Meta:
      model = Profesor
      fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):
   class Meta:
      model = Estudiante
      fields = '__all__'