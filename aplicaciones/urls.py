from django.urls import path
from .views import home, Datos, galeria, agregar_paciente, Listar_Pacientes, modificar_paciente, registro #importamos las funciones creadas en views(aplicaciones)

urlpatterns = [
    path('', home, name='home'), 
    path('Datos/', Datos, name='Datos'), 
    path('galeria/', galeria, name='galeria'), 
    path('addpaciente/', agregar_paciente, name="agregar_paciente"),
    path('lista_pacientes/', Listar_Pacientes, name="Listar_Pacientes"),
    path('modificar-paciente/<id>/', modificar_paciente, name="modificar_paciente"),
    path('registro/', registro, name="registro"),
]

