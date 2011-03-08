from django import forms
from models import SubCategoria, Gasto, Categoria, Ingreso
from django.contrib.auth.models import User
class SubCategoriaForm(forms.ModelForm):
    class Meta:
        model = SubCategoria
        exclude = ("user",)


class GastoForm(forms.ModelForm):
    def __init__(self,username, *args, **kwargs):
        super(GastoForm,self).__init__(*args,**kwargs)
        self.fields["subcategoria"].queryset = SubCategoria.objects.filter(user = username)

    class Meta:
        model = Gasto
        exclude = ("user",)

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        exclude = ("user",)

class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso
        exclude = ("user",)
