from django.conf.urls import url
from django.urls import path

from gestion import views
from gestion.views import *

urlpatterns = [
    path('welcome', view=index),
    path('accueil', view=accueil, name='accueil')

   # url('form', view=ajoutEmploye),


]
