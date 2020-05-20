from django.conf.urls import url
from gestion.views import *

urlpatterns = [
    url('welcome', view=index),
    url('accueil', view=accueil, name='accueil')

]
