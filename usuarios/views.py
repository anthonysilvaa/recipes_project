from django.shortcuts import render

def login(request):
    return render(request, 'usuarios/login.html')

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def dashboard(request):
    return render(request, 'usuarios/dashboard.html')

def logout(request):
    return render(request, 'usuarios/logout.html')
