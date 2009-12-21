from django.conf.urls.defaults import *

urlpatterns = patterns('misgastos.gastos.views',
     url("^$", 'index', name = "index"),
     url("^add$", 'add_gasto', name = "add_gasto"),
     url("^edit/(?P<id>\d)$", 'edit_gasto', name = "edit_gasto"),
     url("^del/(?P<id>\d)$", 'del_gasto', name = "del_gasto"),
       
     
     url("^tipos$", 'list_tipos', name = "list_tipos"),
     url("^tipos/nuevo$", 'add_tipo', name = "add_tipo"),
     url("^tipos/edit/(?P<tipo>\w.*)$", 'edit_tipo', name = "edit_tipo"),
     url("^tipos/del/(?P<tipo>\w.*)$", 'del_tipo', name = "del_tipo"),
     
     
     url("^categorias$", 'list_categorias', name = "list_categorias"),
     url("^categorias/nuevo$", 'add_categoria', name = "add_categoria"),
     url("^categorias/edit/(?P<nombre>\w.*)$", 'edit_categoria', name = "edit_categoria"),
     url("^cateorias/del/(?P<nombre>\w.*)$", 'del_categoria', name = "del_categoria"),
)