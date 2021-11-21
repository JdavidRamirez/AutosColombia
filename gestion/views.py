from django.http import HttpResponse, request
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from gestion.models import Celda, Usuario, Vehiculo



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
        #mensaje2="Vehiculo buscado: %r" %request.GET["vh"]
        vehiculo=request.GET["vh"]
        vehiculos=Vehiculo.objects.filter(placa__icontains=vehiculo)

        return render(request, "resultados_vehiculos.html", {"vehiculos": vehiculos, "query":vehiculo})

    else: 
        mensaje2="No has introducido nada"
    return HttpResponse(mensaje2)

def buscar_celda(request):

    if request.GET["celda"]:
        #mensaje3="Celda buscado: %r" %request.GET["celda"]
        celda=request.GET["celda"]
        celdas=Celda.objects.filter(idCelda__icontains=celda)
        return render(request, "resultados_celdas.html", {"celdas": celdas, "query":celda})
    else: 
        mensaje3="No has introducido nada"
    return HttpResponse(mensaje3)