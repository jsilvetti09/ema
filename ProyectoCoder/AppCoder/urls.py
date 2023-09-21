from django.urls import path
from .views import *

        
urlpatterns = [
    path("inicio/", inicio),
    path("cursos/", ver_cursos),
    path("profes/", ver_profes),
    path("entregas/", ver_entregas),
    path("estudiantes/", ver_estudiantes),
]
