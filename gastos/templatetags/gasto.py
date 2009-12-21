from django import template
from misgastos.gastos.models import Gasto

register = template.Library()
import datetime
    
@register.simple_tag
def total(username):
    total = 0
    for g in Gasto.objects.all():
        total += g.importe
    return total
   
@register.simple_tag
def echomonth(count, forma_string):
    date = datetime.datetime.now()
    m = date.month - count
    return datetime.datetime(date.year,m,date.day).strftime(forma_string)

    
    
@register.simple_tag  
def totalmonth(username, count):
    total = 0
    date = datetime.datetime.now()
    for g in Gasto.objects.filter(fecha__month=date.month - count, fecha__year = date.year):
        total += g.importe
    return total