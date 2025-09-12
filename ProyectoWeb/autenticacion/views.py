from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
class VRegistro(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registro/registro.html', {'form': form}) #me renderiza el html con el formulario de usercreationform pasado como parametro

    def post(self, request):
        
        form = UserCreationForm(request.POST) #Capturo los datos del formulario, usuario y pass
        if form.is_valid():
            usuario = form.save() #Guardo el usuario en la base de datos
            login(request, usuario) #Logueo al usuario recien creado
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg]) #Muestro los mensajes de error que me tira el formulario
                return render(request, 'registro/registro.html', {'form': form}) #Muestrame el formulario pero con los errores

def cerrar_sesion(request):
    logout(request)
    return redirect('home')


def logear(request):
    
    if request.method == 'POST':
        # form = AuthenticationForm()
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=contrasenia)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, 'Usuario no valido')
        else:
            messages.error(request, 'Informacion Incorrecta')

    form = AuthenticationForm()
    return render(request, 'login/login.html', {'form': form})