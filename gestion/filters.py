import django_filters
from .models import *


class Salfilter(django_filters.FilterSet):
    class Meta:
        model = Salarie
        fields = ['matricule', 'nom', 'departement']