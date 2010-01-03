from django.db import models
from django.contrib.auth.models import User




class Categoria(models.Model):
    nombre  = models.CharField(max_length = 40 )

    user    = models.ForeignKey(User, unique = True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, editable=False)
    def __unicode__(self):
        return self.nombre

class Tipo(models.Model):
    nombre  = models.CharField(max_length = 40 )

    user    = models.ForeignKey(User, unique = True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, editable=False)
    def __unicode__(self):
        return self.nombre

class Gasto(models.Model):
    fecha     = models.DateField( blank = False, null = False)
    tipo      = models.ForeignKey(Tipo)
    categoria = models.ForeignKey(Categoria)
    concepto  = models.CharField(help_text = "<span class='tiny'>Nombre del gasto</span>", max_length = 40, blank = False, null = False)
    importe   = models.FloatField(help_text = "<span class='tiny'>Cantidad de $</span> ", blank = False, null = False)
    nota      = models.TextField(blank = True)

    user      = models.ForeignKey(User, unique = True)
    created   = models.DateTimeField(auto_now=False, auto_now_add=True,editable=False)
    updated   = models.DateTimeField(auto_now=True, auto_now_add=False, editable=False)
    def __unicode__(self):
        return self.concepto

