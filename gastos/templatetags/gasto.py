from django import template
from misgastos.gastos.models import Gasto

register = template.Library()
import datetime
from dateutil.relativedelta import relativedelta 

@register.simple_tag
def total(username):
    total = 0
    for g in Gasto.objects.filter(user__username=username):
        total += g.importe
    return total

@register.simple_tag
def graphmonth(count, username):
    date = datetime.datetime.now()
    newdate = datetime.timedelta(days=-30* int(count))
    ndate = date+newdate
    date_ini = datetime.datetime(ndate.year,ndate.month,1)
    date_fin = date_ini + relativedelta(months=1) - relativedelta(days=1)
    r = Gasto.objects.filter(fecha__range= (date_ini,date_fin)).values_list('importe', flat=True)
    return r


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
