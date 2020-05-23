from django.conf.urls import url
from gestion.views import *

urlpatterns = [
    url('welcome', view=index, name='welcome'),
    url('logout', view=deconnexion, name='logout'),
    url('register', view=registration, name='register'),
    url('accueil', view=accueil, name='accueil'),
    url('add/',view=ajoutEmploye, name='add'),
    url('lesSalaries',view=listeSalaries, name='all'),
    url('getEMpl/(?P<pk>.+)', view=calculSalaireNet, name='getsal'),
    url('infoBulletin', view=infoBulletin, name='infoBulletin'),
    url('updateSal/(?P<pk>.+)/', view=modifierSalarie, name="updateSal"),
    url('deleteSal/(?P<pk>.+)/', view=deleteSalarie, name="deleteSal"),


]
