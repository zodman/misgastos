from django import forms
from models import Tipo, Gasto, Categoria
from django.contrib.auth.models import User
class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        exclude = ("user",)


class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        exclude = ("user",)

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        exclude = ("user",)