from gestion.forms import SalForm, BulletinForm
from gestion.models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='gestion:welcome')
def accueil(request):
    return render(request, "accueil.html")


def index(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('gestion:accueil')

        else:
            messages.error(request, "mot de pass ou login incorrects")

    return render(request, "login.html")


def deconnexion(request):
    logout(request)
    return redirect('gestion:welcome')


@login_required(login_url='gestion:welcome')
def ajoutEmploye(request):
    form = SalForm()
    if request.method == 'POST':
        form = SalForm(request.POST)
        form.save()
        messages.success(request, 'bien ajoute')
    return render(request, "addSalarie.html", {'form': form})


@login_required(login_url='gestion:welcome')
def listeSalaries(request):
    liste = Salarie.objects.all()
    return render(request, "listeSalaries.html", {'salaries': liste})


@login_required(login_url='index')
def getSalarie(request, id):
    u = Salarie.objects.get(id=id)
    return render(request, "getSalarie.html", {"user": u})


@login_required(login_url='gestion:welcome')
def registration(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'votre compte a été bien ajouté !')
            return redirect('gestion:welcome')
    return render(request, "register.html", {'form': form})


@login_required(login_url='gestion:welcome')
def infoBulletin(request):
    form = BulletinForm()
    if request.method == 'POST':
        form = BulletinForm(request.POST)
        form.save()
        messages.success(request, 'information bien ajouté')
    return render(request, "addSalarie.html", {'form': form})



