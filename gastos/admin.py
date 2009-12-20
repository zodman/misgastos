from django.contrib import admin
from misgastos.gastos.models import Tipo, Gasto, Categoria

admin.site.register(Tipo)
admin.site.register(Gasto)
admin.site.register(Categoria)