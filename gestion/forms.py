from django import forms
from gestion.models import *


class salForm(forms.ModelForm):
    class Meta:
        model = Salarie
        fields = '__all__'


class BulletinForm(forms.ModelForm):
    class Meta:
        model = BulletinPaie
        fields = '__all__'