from django.db import models

# Create your models here.
class Paciente(models.Model):
    Nombre = models.CharField(max_length=50)
    Edad = models.CharField(max_length=50)
    Sexo = models.CharField(max_length=50)
    Direcion = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)
    Fecha_de_consulta = models.CharField(max_length=50)
    def __str__(self):
        return self.Nombre

class Tratamiento(models.Model):
    Nombre = models.CharField(max_length=50)
    Tratamiento = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=50)
    Fecha_de_cita = models.DateField(max_length=50)
    imagen = models.ImageField(upload_to="Perfiles", blank=True, null=True)
    def __str__(self):
        return self.Nombre

opciones_estado_civil = [
    [0, "Soltero"],
    [1, "Casado"]
]   
opciones_sexo = [
    [2, "Hombre"],
    [3, "Mujer"]
]       

class Datos(models.Model):
    NOMBRE = models.CharField(max_length=50)
    EDAD = models.CharField(max_length=50)
    DIRECCION = models.CharField(max_length=50)
    TELEFONO = models.CharField(max_length=50)
    estado_civil = models.IntegerField(choices=opciones_estado_civil)
    sexo = models.IntegerField(choices=opciones_sexo)
    Padece_de_alguna_enfermedad = models.CharField(max_length=50)
    Toma_algun_tipo_de_medicamento = models.CharField(max_length=50)
    FECHA_EXAMEN = models.CharField(max_length=50)
    Informacion_Adicional_Sobre_el_paciente = models.TextField(max_length=50)

    def __str__(self):
        return self.NOMBRE

