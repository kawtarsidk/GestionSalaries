from django import forms
from gestion.models import *


class EmpForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = '__all__'
