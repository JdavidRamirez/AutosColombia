from django.http import HttpResponse, request
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from gestion.models import Usuario, Vehiculo



def formulario_consulta(request):

    return render(request, "formulario_consulta.html")

def buscar(request):

    if request.GET["user"]:
        #mensaje="Usuario buscado: %r" %request.GET["user"]
        usuario=request.GET["user"]

        clientes=Usuario.objects.filter(nombre__icontains=usuario)

        return render(request, "resultados_busqueda.html", {"clientes": clientes, "query":usuario})
    else:
        mensaje="No has introducido nada"

    return HttpResponse(mensaje)

def buscar_vehiculo(request):

    if request.GET["vh"]:
        mensaje2="Vehiculo buscado: %r" %request.GET["vh"]
    else: 
        mensaje2="No has introducido nada"
    return HttpResponse(mensaje2)

def buscar_celda(request):

    if request.GET["celda"]:
        mensaje3="Celda buscado: %r" %request.GET["celda"]
    else: 
        mensaje3="No has introducido nada"
    return HttpResponse(mensaje3)