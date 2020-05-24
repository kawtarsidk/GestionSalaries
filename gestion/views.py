from gestion.forms import BulletinForm, salForm
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
    form = salForm()
    if request.method == 'POST':
        form = salForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'bien ajoute')
    return render(request, "addSalarie.html", {'form': form})


@login_required(login_url='gestion:welcome')
def listeSalaries(request):
    liste = Salarie.objects.all()
    return render(request, "listeSalaries.html", {'salaries': liste})


def registration(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'votre compte a été bien ajouté !')
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


@login_required(login_url='gestion:welcome')
def modifierSalarie(request, pk):
    salaries = Salarie.objects.get(id=pk)
    form = salForm(instance=salaries)

    if request.method == 'POST':
        form = salForm(request.POST, instance=salaries)
        if form.is_valid():
            form.save()
            return redirect('gestion:all')

    context = {'form': form}
    return render(request, 'addSalarie.html', context)


@login_required(login_url='gestion:welcome')
def deleteSalarie(request, pk):
    salarie = Salarie.objects.get(id=pk)
    if request.method == "POST":
        salarie.delete()
        return redirect('gestion:all')

    context = {'item': salarie}
    return render(request, 'deleteSalarie.html', context)


@login_required(login_url='index')
def calculSalaireNet(request, pk):
    s = Salarie.objects.get(id=pk)
    if s.Anciennete < 2:
        primeAnciennete = 0
    elif s.Anciennete > 2 & s.Anciennete < 5:
        primeAnciennete = s.salaireBase*0.05
    elif s.Anciennete > 5 & s.Anciennete < 12:
        primeAnciennete = s.salaireBase * 0.1
    elif s.Anciennete > 12 & s.Anciennete < 20:
        primeAnciennete = s.salaireBase * 0.15
    elif s.Anciennete > 20 & s.Anciennete < 25:
        primeAnciennete = s.salaireBase * 0.2
    else:
        primeAnciennete = s.salaireBase * 0.25

    salaireBrut = s.salaireBase + primeAnciennete + s.bulletinPaie.prime

    if salaireBrut <= 6000:
        cnss = salaireBrut * s.bulletinPaie.p_cnss
    else:
        cnss = 6000 * s.bulletinPaie.p_cnss

    if salaireBrut == 2500:
        impot = salaireBrut * 0
    elif 2500 < salaireBrut < 4167:
        impot = salaireBrut * 0.1
    elif 4166 < salaireBrut < 5001:
        impot = salaireBrut * 0.2
    elif 5000 < salaireBrut < 6667:
        impot = salaireBrut * 0.3
    elif 6666 < salaireBrut < 15001:
        impot = salaireBrut * 0.34
    else:
        impot = salaireBrut * 0.38

    impot = round(impot,2)
    cimr = salaireBrut * s.bulletinPaie.p_cimr
    salaireNet = salaireBrut - cnss - cimr - impot

    return render(request, 'getSalarie.html', {"user": s, 'primeAnciennete': primeAnciennete, 'salaireBrut': salaireBrut, 'cnss': cnss, 'cimr': cimr, 'impot': impot, 'salaireNet': salaireNet})

def documentation (request):
        return render(request,"Documentation.html")
