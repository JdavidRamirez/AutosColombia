from import_export import resources
from .models import Usuario,Pago, Vehiculo,Celda



class PersonResource(resources.ModelResource):
    class Meta:
        model = Usuario
        model = Pago
        model=Vehiculo
        model=Celda