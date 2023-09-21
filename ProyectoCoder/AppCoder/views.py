from django.shortcuts import render
from django.http import HttpResponse
from .models import Profesor


# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def ver_cursos(request):
    return render (request, "AppCoder/ver_cursos.html")

def ver_profes(request):
    return render (request, "AppCoder/ver_profes.html")

def ver_entregas(request):
    return render (request, "AppCoder/ver_entregas.html")

def ver_estudiantes(request):
    return render (request, "AppCoder/ver_estudiantes.html")