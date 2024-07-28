from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Curso, Estudiante, Profesor
from .form import CursoForm
from rest_framework import viewsets
from .serializers import CursoSerializer, EstudianteSerializer, ProfesorSerializer
from rest_framework.decorators import api_view

def index(request):
   return HttpResponse("Hola estudiante")

def curso(request, name):
   return HttpResponse(f"Bienvenido {name} al curso")

def cursoFormView(request):
   form = CursoForm(request.POST)
   if form.is_valid():
      form.save()
   return render(request, "form_curso.html", {"form": form})

class CursosViewSet(viewsets.ModelViewSet):
   queryset = Curso.objects.all()
   serializer_class = CursoSerializer

def profesores(request):
   profesoresList = Profesor.objects.all() 
   return render(request, "profesores.html", {"profesores": profesoresList})

class ProfesoresViewSet(viewsets.ModelViewSet):
   queryset = Profesor.objects.all()
   serializer_class = ProfesorSerializer

class EstudiantesViewSet(viewsets.ModelViewSet):
   queryset = Estudiante.objects.all()
   serializer_class = EstudianteSerializer

@api_view(['GET'])
def curso_count(request):
   """
   Cuenta la cantidad de cursos
   """
   try:
      cantidad = Curso.objects.count()
      return JsonResponse(
            {
                "cantidad_cursos": cantidad
            },
            safe=False,
            status=200,
        )
   except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )


# Create your views here.
