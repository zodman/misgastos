from django.db import models
from django.contrib.auth.models import User

class SubCategoria(models.Model):
    nombre  = models.CharField(max_length = 40 )
    user    = models.ForeignKey(User)
    created = models.DateTimeField(auto_now=False, auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, editable=False)
    def __unicode__(self):
        return self.nombre

class Categoria(models.Model):
    nombre  = models.CharField(max_length = 40 )
    subcategorias = models.ManyToManyField(SubCategoria, related_name='categorias')
    user    = models.ForeignKey(User)
    created = models.DateTimeField(auto_now=False, auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, editable=False)
    def __unicode__(self):
        return self.nombre

class Gasto(models.Model):
    fecha     = models.DateField( blank = False, null = False)
    subcategoria = models.ForeignKey(SubCategoria, related_name='gastos')
    concepto  = models.CharField(help_text = "<span class='tiny'>Nombre del gasto</span>", max_length = 40, blank = False, null = False)
    importe   = models.FloatField(help_text = "<span class='tiny'>Cantidad de $</span> ", blank = False, null = False)
    nota      = models.TextField(blank = True)

    user      = models.ForeignKey(User)
    created   = models.DateTimeField(auto_now=False, auto_now_add=True,editable=False)
    updated   = models.DateTimeField(auto_now=True, auto_now_add=False, editable=False)
    def __unicode__(self):
        return self.concepto

OPCIONES = (
    (1,"Estatico"),
    (15,"Quincenal"),
    (30,"Mensual")
)
class Ingreso(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.IntegerField(choices = OPCIONES)
    user = models.ForeignKey(User,related_name="ingresos")
    importe = models.FloatField()

    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    created   = models.DateTimeField(auto_now=False, auto_now_add=True,editable=False)
    updated   = models.DateTimeField(auto_now=True, auto_now_add=False, editable=False)
    def __unicode__(self):
        return self.nombre

