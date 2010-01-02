from misgastos.gastos.models import Tipo, Categoria, Gasto
from django.views.generic.list_detail import object_list
from django.views.generic.simple import direct_to_template
from django.views.generic.create_update import create_object, update_object, delete_object
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404


###########################################3
def list_tipos(request):
    queryset = Tipo.objects.all()
    return object_list(request, queryset = queryset)

def edit_tipo(request, tipo):
    t = get_object_or_404(Tipo,nombre = tipo)
    return update_object(request, model = Tipo, object_id = t.id )

def add_tipo(request):
    return create_object(request,model = Tipo, post_save_redirect = reverse('list_tipos'))

def del_tipo(request, tipo):
    tipo = Tipo.objects.filter(nombre = tipo)
    tipo.delete()
    return HttpResponseRedirect(reverse('list_tipos'))
###########################################
def list_categorias(request):
    queryset = Categoria.objects.all()
    return object_list(request, queryset = queryset)

def edit_categoria(request, nombre):
    cat = get_object_or_404(Categoria, nombre = nombre)
    return update_object(request, model = Categoria, object_id = cat.id )

def add_categoria(request):
    return create_object(request,model = Categoria, post_save_redirect = reverse('list_categorias'))

def del_categoria(request, nombre):
    cat = Categoria.objects.filter(nombre = nombre)
    cat.delete()
    return HttpResponseRedirect(reverse('list_categorias'))
 ##############################################################

def index(request):
    gastos = Gasto.objects.all()
    return object_list(request, queryset = gastos)

def add_gasto(request):
     return create_object(request,model = Gasto, post_save_redirect = reverse('index'))

def edit_gasto(request, id):
    g = get_object_or_404(Gasto, id = id)
    return update_object(request, model = Gasto, object_id = g.id , post_save_redirect = reverse('index'))

def del_gasto(request, id):
    g = get_object_or_404(Gasto, id = id)
    g.delete()
    return HttpResponseRedirect(reverse('index'))