from django import template
from misgastos.gastos.models import Gasto

register = template.Library()
import datetime

@register.simple_tag
def total(username):
    total = 0
    for g in Gasto.objects.filter(user__username=username):
        total += g.importe
    return total

@register.simple_tag
def echomonth(count, forma_string):
    date = datetime.datetime.now()
    newdate = datetime.timedelta(days=-30* int(count))
    return (date + newdate).strftime(forma_string)

@register.simple_tag
def totalmonth(username, count):
    total = 0
    date = datetime.datetime.now()
    newdate = datetime.timedelta(days=-30* int(count))
    d = date + newdate
    for g in Gasto.objects.filter(user__username=username,fecha__month=d.month, fecha__year = d.year):
        total += g.importe
    return total
