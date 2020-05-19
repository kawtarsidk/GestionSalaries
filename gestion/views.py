
from gestion.models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect


def checkCompte(login, password):

    compte = Compte.objects.all()
    for c in compte:
        if c.login == login and c.password == password:
            return 'true'
        else:
            return 'false'


def index(request):

    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        if checkCompte(login, password) == "true":
           # return HttpResponse('c est un compte')
            return render(request, "accueil.html")
        else:
            return HttpResponse('erreur')

    return render(request, "login.html")


