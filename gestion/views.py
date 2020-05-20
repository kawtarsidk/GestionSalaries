from django.contrib.auth import authenticate, login, logout

from gestion.models import *
from django.contrib import messages
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
        username = request.POST.get('username')
        password = request.POST.get('password')

        compte = authenticate(request, username=username, password=password)

        if compte is not None:
            login(request, compte)
            return HttpResponse("vous etes connecte")
        else:
            return HttpResponse("erreur")

    return render(request, "login.html")




