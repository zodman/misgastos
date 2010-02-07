from django import forms
from models import Tipo, Gasto, Categoria
from django.contrib.auth.models import User
class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        exclude = ("user",)


class GastoForm(forms.ModelForm):
    def __init__(self,username, *args, **kwargs):
	super(GastoForm,self).__init__(*args,**kwargs)
	self.fields["categoria"].queryset = Categoria.objects.filter(user = username)
	self.fields["tipo"].queryset = Tipo.objects.filter(user = username)

    class Meta:
        model = Gasto
        exclude = ("user",)

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        exclude = ("user",)
