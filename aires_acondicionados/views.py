from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import UserCreationForm
from .models import Servicios,Catalogo
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'aires/index.html', {})

def servicios(request):
    return render(request, 'aires/servicios.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

def servicios2(request):
        user = request.user
        Nombres = request.POST['txtNombres']
        Email = request.POST['txtEmail']
        Telefono = request.POST['txtTelefono']
        Ubicacion = request.POST['txtUbicacion']
        Zip = request.POST['txtZip']
        Fecha = request.POST['txtFecha']
        # Hora = request.POST['txtHora'+'txtMinuto'+'txtTiempo'] 
        s = Servicios(Usuario=user,Nombres=Nombres,Email=Email,Telefono=Telefono,Ubicacion=Ubicacion,
        ZipCode=Zip,Fecha=Fecha)
        s.save()
        return render(request, 'aires/servicios2.html', {'Nombres': Nombres})

def catalogo(request):  
    #Obtenemos los departamentos ordenados de manera descendente.
    #[Z-A] Se antepone el signo menos (-)
    cargarCatalogo = Catalogo.objects.all()

    #Cargamos el archivo index.html que se encuentra en la carpeta 'templates'
    template = loader.get_template('aires/catalogo.html')

    #Creamos el nombre 'deptos' para reutilizarlo en el archivo 'index.html'
    context = {
        'catalogo': cargarCatalogo,
    }

    #Invocamos la página de respuesta 'index.html'
    return HttpResponse(template.render(context, request))  