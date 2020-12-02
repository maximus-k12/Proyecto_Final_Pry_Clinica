from django import forms
from .models import Datos, Tratamiento, Paciente
from django.contrib.auth.forms import UserCreationForm

class DatosForm(forms.ModelForm):
    #nombre =forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Datos
        #fields = ["NOMBRE", "EDAD", "FECHA_EXAMEN"]
        fields = '__all__'

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Tratamiento
        fields = '__all__'


class PaForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = '__all__'

class CustomUserCreationsForm(UserCreationForm):
    pass