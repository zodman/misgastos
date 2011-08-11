from django.views.generic.list_detail import object_list
from django.views.generic.simple import direct_to_template
from django.views.generic.create_update import create_object, update_object, delete_object
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.template import RequestContext

import datetime


from misgastos.gastos.models import SubCategoria, Categoria, Gasto,Ingreso
from misgastos.gastos.forms import GastoForm, SubCategoriaForm, CategoriaForm, IngresoForm

def find_model(request,id,Model):
    i = get_object_or_404(Model,id = id)
    if i.user != request.user:
        raise Http404
    return i


###########################################3
@login_required
def list_tipos(request):
    queryset = SubCategoria.objects.filter(user= request.user)
    return object_list(request, queryset = queryset)


@login_required
def edit_tipo(request, tipo):
    t = find_model(request,tipo,SubCategoria)
    if request.POST:
        f = SubCategoriaForm(request.POST,instance = t)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect(reverse('list_tipos'))
        else:
            return render_to_response("gastos/tipo_form.html", dict(form=f))
    else:
        f = SubCategoriaForm(instance = t)
    return render_to_response("gastos/tipo_form.html", dict(form=f),
            context_instance=RequestContext(request)
        )


@login_required
def add_tipo(request):
    if request.POST:
        formtipo = SubCategoriaForm(request.POST)
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
        formtipo = SubCategoriaForm()
    return render_to_response("gastos/tipo_form.html", dict(form=formtipo),
            context_instance=RequestContext(request)
        )


@login_required
def del_tipo(request, tipo):
    tipo = SubCategoria.objects.filter(user = request.user,id = tipo)
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
            catform.save_m2m()
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
    gastos = Gasto.objects.filter(user = request.user ).order_by("fecha")
    return object_list(request, queryset = gastos)

@login_required
def add_gasto(request):
    if request.POST:
        gastoform = GastoForm(request.user, request.POST)
        if not gastoform.is_valid():
           return render_to_response("gastos/gasto_form.html", dict(form = gastoform),context_instance=RequestContext(request))
        else:
            gast = gastoform.save(commit=False)
            gast.user = request.user
            gast.save()
            gastoform.save_m2m()
            return HttpResponseRedirect(reverse('index'))
    else:
        gastoform = GastoForm(request.user)
    return render_to_response("gastos/gasto_form.html", dict(form = gastoform),
            context_instance=RequestContext(request)
        )


@login_required
def edit_gasto(request, id):
    g = find_model(request,id,Gasto)
    if request.POST:
        gastoform = GastoForm(request.user, request.POST, instance = g)
        if not gastoform.is_valid():            
            return render_to_response("gastos/gasto_form.html", dict(form = gastoform), context_instance=RequestContext(request))
        else:
            gast = gastoform.save(commit=False)
            gast.save()
            gastoform.save_m2m()
            return HttpResponseRedirect(reverse('index'))
    else:
        gastoform = GastoForm(request.user, instance = g )
    return render_to_response("gastos/gasto_form.html", dict(form = gastoform),
            context_instance=RequestContext(request)
        )


@login_required
def del_gasto(request, id):
    g = find_model(request,id,Gasto)
    g.delete()
    return HttpResponseRedirect(reverse('index'))


################
@login_required
def change_month(request):
    from misgastos import settings
    number = request.GET.get("number",settings.MONTH)
    profile = request.user.get_profile()
    profile.number_months = int(number)
    profile.save()
    return  HttpResponse("Success")
##############
@login_required
def list_ingresos(request):
    return object_list(request,Ingreso.objects.filter(user = request.user))
@login_required
def create_ingresos(request):
    if request.POST:
        f = IngresoForm(request.POST)
        if f.is_valid():
            i = f.save(commit = False)
            i.user = request.user
            i.save()
            return HttpResponseRedirect(reverse("list_ingresos"))
        else:
            return render_to_response("gastos/gasto_form.html", 
                dict(form = f),context_instance =RequestContext(request)
                )
    return create_object(request, form_class=IngresoForm)

@login_required
def edit_ingreso(request,id_ingreso):
    i =find_model(request,id_ingreso,Ingreso)
    return update_object(request,object_id= id_ingreso,model=Ingreso,post_save_redirect=reverse("list_ingresos"))
@login_required
def del_ingreso(request,id_ingreso):
    i = find_model(request,id_ingreso,Ingreso)
    i.delete()
    return HttpResponseRedirect(reverse("list_ingresos"))

@login_required
def show_balance(request):
    from templatetags.gasto import graphmonth,echomonth,graph_ingreso
    profile = request.user.get_profile()
    gasto_mensual = dict()
    ingreso_mensual =dict()
    for i in profile.get_number_months():
        key = echomonth(i,"%B-%Y")
        total = 0
        total_ingreso = 0
        for g in graphmonth(i,request.user.username):
            total = total + g

        for i in  graph_ingreso(i,request.user.username):
            total_ingreso = total_ingreso + i

        gasto_mensual[key] = total
        ingreso_mensual[key] = total_ingreso

    gasto_mensual = [(fecha,importe) for fecha,importe in gasto_mensual.items()]
    gasto_mensual.sort()
    ingreso_mensual = [(fecha,importe) for fecha,importe in ingreso_mensual.items()]
    ingreso_mensual.sort()
    
    return render_to_response("balance.html", dict(gastos = gasto_mensual, ingresos=ingreso_mensual), 
        context_instance = RequestContext(request) )
