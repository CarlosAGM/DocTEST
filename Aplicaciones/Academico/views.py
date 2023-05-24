# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Aplicaciones.Academico.forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')

def interfaz(request):
    return render(request, 'interfaz.html')

def cedula(request):
    return render(request, 'cedula.html')

def automotriz(request):
    return render(request, 'automotriz.html')

def qr(request):
    return render(request, 'qr.html')
