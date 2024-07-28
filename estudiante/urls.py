
from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("cursos", views.CursosViewSet)
router.register("profesores", views.ProfesoresViewSet)
router.register("", views.EstudiantesViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('curso/create/', views.cursoFormView, name='cursoCreate'),
   path('curso/cantidad/', views.curso_count, name='cantidad_cursos'),
   path('curso/<str:name>/', views.curso, name='curso'),
   path('profesor/index/', views.profesores, name='profesores'),
   path('saludo/index/', views.index)
]