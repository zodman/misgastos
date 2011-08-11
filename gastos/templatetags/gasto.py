from django import template
from misgastos.gastos.models import Gasto,Ingreso

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
    newdate = datetime.timedelta(days=-30 * int(count))
    ndate = date+newdate
    date_ini = datetime.datetime(ndate.year,ndate.month,1)
    date_fin = date_ini + relativedelta(months=1) - relativedelta(days=1)
    r = Gasto.objects.filter(user__username = username,fecha__range= (date_ini,date_fin)).values_list('importe', flat=True).order_by("fecha")
    return r

def graph_ingreso(count,username):
    date = datetime.datetime.now()
    newdate = datetime.timedelta(days=-30 * int(count))
    ndate = date+newdate
    date_ini = datetime.datetime(ndate.year,ndate.month,1)
    date_quincena = datetime.datetime(ndate.year,ndate.month,15)
    date_fin = date_ini + relativedelta(months=1) - relativedelta(days=1)
    ingresos_estaticos = Ingreso.objects.filter(
        tipo =1,user__username = username,
        fecha_inicio__range = (date_ini,date_fin)
        ).values_list("importe",flat = True).order_by("fecha_inicio")
    sql = """
    SELECT importe FROM "gastos_ingreso" 
        INNER JOIN "auth_user" ON ("gastos_ingreso"."user_id" = "auth_user"."id") 
        WHERE "auth_user"."username" = "%s"  AND 
        "gastos_ingreso"."tipo" = "%s" and 
        ( "%s" between "gastos_ingreso"."fecha_inicio" and "gastos_ingreso"."fecha_fin"   or
         "%s" between "gastos_ingreso"."fecha_inicio" and "gastos_ingreso"."fecha_fin"  
        )
    """ % ( username,"15",date_quincena,date_fin)
    from django.db import connection,transaction
    cursor = connection.cursor()
    cursor.execute(sql)
    transaction.commit_unless_managed()
    rows = cursor.fetchall()
    ingresos_quincenales = [ i[0] for i in rows]
    return ingresos_quincenales + list(ingresos_estaticos)



@register.simple_tag
def echomonth(count, forma_string):
    date = datetime.datetime.now()
    newdate = datetime.timedelta(days=-30* int(count))
    return (date + newdate).strftime(forma_string.encode("ascii"))

@register.simple_tag
def totalmonth(username, count):
    total = 0
    date = datetime.datetime.now()
    newdate = datetime.timedelta(days=-30* int(count))
    d = date + newdate
    for g in Gasto.objects.filter(user__username=username,fecha__month=d.month, fecha__year = d.year):
        total += g.importe
    return total
