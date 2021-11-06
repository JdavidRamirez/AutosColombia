from django.contrib import admin
from .models import Usuario, Pago, Vehiculo, Celda
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from gestion.models import *



admin.site.register(Usuario)
admin.site.register(Pago)
admin.site.register(Vehiculo)
admin.site.register(Celda)
