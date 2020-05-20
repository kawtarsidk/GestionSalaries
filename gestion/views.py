from gestion.forms import EmpForm
from gestion.models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth import authenticate,login, logout
from .urls import *

def accueil(request):
    return render(request, "accueil.html")

def index(request):
    if request.method == 'POST':
        uname = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=uname, password=password)
        if user is not None:
            login(request,user)
            return  redirect('gestion:accueil')

        else:
            messages.error(request,"mot de pass ou login incorrects")

    return render(request, "login.html")


def ajoutEmploye(request):
    form = EmpForm()
    if request.method == 'POST':
        form = EmpForm(request.POST)
        form.save()
        messages.success(request, 'bien ajoute')
    return render(request, "accueil.html", {'form': form})