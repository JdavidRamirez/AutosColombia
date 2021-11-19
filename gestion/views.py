from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from gestion.models import Usuario


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def busqueda_usuarios(request):

    return render(request, "busqueda_usuarios.html")
