from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Usuario(models.Model):
    idUsuario=models.PositiveSmallIntegerField(primary_key=True)
    cedula=models.CharField(max_length=10)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    celular=models.CharField(max_length=15)
    email=models.CharField(max_length=50)

    def nombre_completo(self):
        return "{}, {}".format(self.apellido, self.nombre)

    def __str__(self):
        return self.nombre_completo()

class Pago(models.Model):
    idPago=models.PositiveSmallIntegerField(primary_key=True)
    fecha=models.DateTimeField('date published')
    idUsuario=models.ForeignKey(
        Usuario, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.idUsuario, self.fecha)

class Vehiculo(models.Model):
    idVehiculo=models.PositiveSmallIntegerField(primary_key=True)
    placa=models.CharField(max_length=6)
    color=models.CharField(max_length=10)
    marca=models.CharField(max_length=10)
    modelo=models.CharField(max_length=10)
    propietario=models.CharField(max_length=50)
    idUsuario=ForeignKey(
        Usuario, null=True, blank=True, on_delete=models.CASCADE)


    def caracteristica(self):
        return "{} {}, {}".format(self.placa, self.propietario, self.idVehiculo)

    def __str__(self):
        return self.caracteristica()

class Celda(models.Model):
    idCelda=models.PositiveSmallIntegerField(primary_key=True)
    dimensiones=models.CharField(max_length=50)
    idVehiculo=ForeignKey(
        Vehiculo, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        texto = "{}, {}"
        return texto.format(self.idCelda, self.idVehiculo)



