from django.db import models
from django.contrib import admin

class Categoria(models.Model):
    nombre  = models.CharField(max_length = 40 )
    created = models.DateTimeField(auto_now=False, auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, editable=False)
    def __unicode__(self):
        return self.nombre
class Tipo(models.Model):
    nombre  = models.CharField(max_length = 40 )
    created = models.DateTimeField(auto_now=False, auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, editable=False)
    def __unicode__(self):
        return self.nombre

class Gasto(models.Model):
    fecha     = models.DateField(auto_now=True, blank = False, null = False)
    concepto  = models.CharField(max_length = 40, blank = False, null = False)
    importe   = models.FloatField(blank = False, null = False)
    Nota      = models.TextField(blank = True)
    tipo      = models.ForeignKey(Tipo)
    categoria = models.ForeignKey(Categoria) 
    created   = models.DateTimeField(auto_now=False, auto_now_add=True,editable=False)
    updated   = models.DateTimeField(auto_now=True, auto_now_add=False, editable=False)
    def __unicode__(self):
        return self.concepto
    
admin.site.register(Tipo)
admin.site.register(Categoria)
admin.site.register(Gasto)