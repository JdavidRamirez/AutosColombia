from django.http import HttpResponse, request
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from gestion.models import Usuario, Vehiculo


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def busqueda_usuarios(request):

    return render(request, "busqueda_usuarios.html")

def buscar(request):
    mensaje="Usuario buscado: %r" %request.GET["user"]
    return HttpResponse(mensaje)

def busqueda_vehiculo(request):

    return render(request, "busqueda_vehiculo.html")

def buscar_vehiculo(request):
    mensaje2="Vehiculo buscado: %r" %request.GET["vh"]
    return HttpResponse(mensaje2)