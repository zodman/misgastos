from django import template
from misgastos.gastos.models import Gasto

register = template.Library()

    
@register.simple_tag
def total(username):
    total = 0
    for g in Gasto.objects.all():
        total += g.importe
    return total
    
    
    