from django.views.generic.list_detail import object_list
from django.views.generic.simple import direct_to_template
from django.views.generic.create_update import create_object, update_object, delete_object
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.template import RequestContext


from misgastos.gastos.models import Tipo, Categoria, Gasto
from misgastos.gastos.forms import GastoForm, TipoForm, CategoriaForm

###########################################3
@login_required
def list_tipos(request):
    queryset = Tipo.objects.filter(user = request.user)
    return object_list(request, queryset = queryset)


@login_required
def edit_tipo(request, tipo):
    t = get_object_or_404(Tipo,id = tipo)
    if request.POST:
        f = TipoForm(request.POST,instance = t)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect(reverse('list_tipos'))
        else:
            return render_to_response("gastos/tipo_form.html", dict(form=f))
    else:
        f = TipoForm(instance = t)
    return render_to_response("gastos/tipo_form.html", dict(form=f),
            context_instance=RequestContext(request)
        )


@login_required
def add_tipo(request):
    if request.POST:
        formtipo = TipoForm(request.POST)
        if formtipo.is_valid():
            tip = formtipo.save(commit=False)
            tip.user = request.user
            tip.save()
            return HttpResponseRedirect(reverse('list_tipos'))
        else:
            return render_to_response("gastos/tipo_form.html",
                dict(form=formtipo)
            )
    else:
        formtipo = TipoForm()
    return render_to_response("gastos/tipo_form.html", dict(form=formtipo),
            context_instance=RequestContext(request)
        )


@login_required
def del_tipo(request, tipo):
    tipo = Tipo.objects.filter(id = tipo)
    tipo.delete()
    return HttpResponseRedirect(reverse('list_tipos'))

###########################################
@login_required
def list_categorias(request):
    queryset = Categoria.objects.filter(user = request.user)
    return object_list(request, queryset = queryset)

@login_required
def edit_categoria(request, nombre):
    cat = get_object_or_404(Categoria, nombre = nombre)
    if request.POST:
        f = CategoriaForm(request.POST, instance = cat )
        if f.is_valid():
            f.save()
            return HttpResponseRedirect(reverse("list_categorias"))
    else:
        f = CategoriaForm(instance = cat)
    return render_to_response("gastos/categoria_form.html", dict(form = f ),
        context_instance=RequestContext(request)
    )

@login_required
def add_categoria(request):
    if request.POST:
        catform = CategoriaForm(request.POST)
        if catform.is_valid():
            cat = catform.save(commit = False)
            cat.user = request.user
            cat.save()
            return HttpResponseRedirect(reverse('list_categorias'))
        else:
            return render_to_response("gastos/categoria_form.html",
                dict( form = catform), context_instance=RequestContext(request)
                )
    else:
        catform = CategoriaForm()
    return render_to_response(
        "gastos/categoria_form.html", dict(form = catform),
        context_instance=RequestContext(request)
    )


@login_required
def del_categoria(request, nombre):
    cat = Categoria.objects.filter(nombre = nombre)
    cat.delete()
    return HttpResponseRedirect(reverse('list_categorias'))


##############################################################
@login_required
def index(request):
    gastos = Gasto.objects.filter(user = request.user )
    return object_list(request, queryset = gastos)

@login_required
def add_gasto(request):
    if request.POST:
        gastoform = GastoForm(request.user, request.POST)
        if not gastoform.is_valid():
           return render_to_response("gastos/gasto_form.html", dict(form = gastoform))
        else:
            gast = gastoform.save(commit=False)
            gast.user = request.user
            gast.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        gastoform = GastoForm(request.user)
    return render_to_response("gastos/gasto_form.html", dict(form = gastoform),
            context_instance=RequestContext(request)
        )


@login_required
def edit_gasto(request, id):
    g = get_object_or_404(Gasto, id = id)
    
    if request.POST:
        gastoform = GastoForm(request.user, request.POST, instance = g)
        if not gastoform.is_valid():
           return render_to_response("gastos/gasto_form.html", dict(form = gastoform))
        else:
            gast = gastoform.save(commit=False)
            return HttpResponseRedirect(reverse('index'))
    else:
        gastoform = GastoForm(request.user, instance = g )
    return render_to_response("gastos/gasto_form.html", dict(form = gastoform),
            context_instance=RequestContext(request)
        )


@login_required
def del_gasto(request, id):
    g = get_object_or_404(Gasto, id = id)
    g.delete()
    return HttpResponseRedirect(reverse('index'))
