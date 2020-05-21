from django.conf.urls import url
from gestion.views import *

urlpatterns = [
    url('welcome', view=index),
    url('accueil', view=accueil, name='accueil'),
    url('add/',view=ajoutEmploye, name='add'),
    url('lesSalaries',view=listeSalaries, name='all'),
    url('getEMpl/(?P<id>.+)', view=getSalarie, name='getsal')


]
