from misgastos.gatos.models import Tipo, Categoria, Gasto

from django.generic.views.list_detail import object_list

def list_tipos(request):
    queryset = Tipo.objects.all()
    return object_list(request, dict(queryset = queryset))
    