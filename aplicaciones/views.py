from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Tratamiento
from .forms import DatosForm, PacienteForm, PaForm, CustomUserCreationsForm 
from django.contrib.auth import authenticate, login



# Create your views here.

def home(request):
    return render(request, 'paginas/home.html')

def Datos(request):
    data = {
        'form': DatosForm()
    }
    if request.method == 'POST':
        formulario = DatosForm(data=request.POST) #aca se obtienen los datos y el formulario queda lleno
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Informacion recibiada"
        else:
            data["form"] = formulario

    return render(request, 'paginas/Datos.html', data)
    
def galeria(request):
    return render(request, 'paginas/galeria.html')

def agregar_paciente(request):
    data = {
        'form': PacienteForm()
     }
    if request.method == 'POST':
        formulario_1 = PacienteForm(data=request.POST, files=request.FILES)
        if formulario_1.is_valid():
            formulario_1.save()
            data["mensaje"] = "Paciente Registrado Correctamente"
        else:
            data["form"] = formulario_1
   
    return render(request, 'paginas/Paciente/agregar.html', data)

def Listar_Pacientes(request):

    tratamiento = Tratamiento.objects.all()

    data = {
        'tratamiento':tratamiento
    }
    return render(request, 'paginas/Paciente/listar.html', data)

def modificar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id = id)
    data= {
        'form': PaForm(instance=paciente)
    }
    if request.method == 'POST':
        formulario = PaForm(data=request.POST, instance=paciente, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="Listar_Pacientes")
        data["form"] = formulario
    return render(request, 'paginas/Paciente/modificar.html', data)

def registro(request):
    data = {
        'form': CustomUserCreationsForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationsForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)