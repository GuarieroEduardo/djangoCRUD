from django.shortcuts import render
from api.models import *

def home(request):
    user = CustonUser.objects.all()
    return render(request, 'home.html', {'usuarios': user})
    

def login(request):
    return render(request, 'login.html')

def criarAluno(request):
    return render(request, 'criarAluno.html')