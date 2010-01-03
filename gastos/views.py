from django.views.generic.list_detail import object_list
from django.views.generic.simple import direct_to_template
from django.views.generic.create_update import create_object, update_object, delete_object
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory


from misgastos.gastos.models import Tipo, Categoria, Gasto
from misgastos.gastos.forms import GastoForm

###########################################3
@login_required
def list_tipos(request):
    queryset = Tipo.objects.all()
    return object_list(request, queryset = queryset)
@login_required
def edit_tipo(request, tipo):
    t = get_object_or_404(Tipo,nombre = tipo)
    return update_object(request, model = Tipo, object_id = t.id )
@login_required
def add_tipo(request):
    if request.POST:
        formtipo = modelformset_factory(Tipo,request.POST, exclude=("user",))
        if formtipo.is_valid():
            tip = formtipo.save(commit=False)
            tip.user = request.user
            tip.save()
            return HttpResponseRedirect(reverse('list_tipos'))
        else:
            return render_to_response("gastos/tipo_form.html", dict(form=formtipo))
    else:
        formtipo = modelformset_factory(Tipo,exclude=("user"))
    return render_to_response("gastos/tipo_form.html", dict(form=formtipo))
#    return create_object(request,model = Tipo, post_save_redirect = reverse('list_tipos'))
@login_required
def del_tipo(request, tipo):
    tipo = Tipo.objects.filter(nombre = tipo)
    tipo.delete()
    return HttpResponseRedirect(reverse('list_tipos'))
###########################################
@login_required
def list_categorias(request):
    queryset = Categoria.objects.all()
    return object_list(request, queryset = queryset)
@login_required
def edit_categoria(request, nombre):
    cat = get_object_or_404(Categoria, nombre = nombre)
    return update_object(request, model = Categoria, object_id = cat.id )
@login_required
def add_categoria(request):
    if request.POST:
        catform = modelformset_factory(Categoria, request.POST, exclude=("user",))
        if catform.is_valid():
            cat = catform.save(commit = False)
            cat.user = request.user
            cat.save()
            return HttpResponseRedirect(reverse('list_categorias'))
        else:
            return render_to_response("gastos/categoria_form.html", dict( form =catform))
    else:
        catform = modelformset_factory(Categoria,exclude=("user",))
    return render_to_response("gastos/categoria_form.html", dict( form =catform))
    #return create_object(request,model = Categoria, post_save_redirect = reverse('list_categorias'))
@login_required
def del_categoria(request, nombre):
    cat = Categoria.objects.filter(nombre = nombre)
    cat.delete()
    return HttpResponseRedirect(reverse('list_categorias'))
 ##############################################################
@login_required
def index(request):
    gastos = Gasto.objects.all()
    return object_list(request, queryset = gastos)
@login_required
def add_gasto(request):
    if request.POST:
        gastoform = GastoForm(request.POST)
        if not gastoform.is_valid():
           return render_to_response("gastos/gasto_form.html", dict(form = gastoform))
        else:
            gast = gastoform.save(commit=False)
            gast.user = request.user
            gast.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        gastoform = GastoForm()
    return render_to_response("gastos/gasto_form.html", dict(form = gastoform))
    #return create_object(request,form_class = GastoForm, post_save_redirect = reverse('index'))
@login_required
def edit_gasto(request, id):
    g = get_object_or_404(Gasto, id = id)
    return update_object(request, model = Gasto, object_id = g.id , post_save_redirect = reverse('index'))
@login_required
def del_gasto(request, id):
    g = get_object_or_404(Gasto, id = id)
    g.delete()
    return HttpResponseRedirect(reverse('index'))
