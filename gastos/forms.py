from django import forms
from models import Tipo, Gasto
from django.contrib.auth.models import User
class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo


class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        exclude = ("user",)
