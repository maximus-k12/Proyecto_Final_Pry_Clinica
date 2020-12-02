from django.contrib import admin
from .models import Tratamiento, Paciente, Datos
# Register your models here.

class PacientesAdmin(admin.ModelAdmin):
    list_display = ["Nombre", "Edad", "Sexo", "Telefono"]
    list_editable = ["Telefono"]
    search_fields = ["Nombre"]

class TratamientoAdmin(admin.ModelAdmin):
    list_display = ["Nombre", "Tratamiento"]
    list_editable = ["Tratamiento"]
    search_fields = ["Nombre"]    

admin.site.register(Tratamiento, TratamientoAdmin)
admin.site.register(Paciente, PacientesAdmin)
admin.site.register(Datos)