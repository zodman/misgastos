from django.conf.urls.defaults import *

urlpatterns = patterns('misgastos.gastos.views',
     url("^$", 'index', name = "index"),
     url("^add$", 'add_gasto', name = "add_gasto"),
     url("^edit/(?P<id>\d.*)$", 'edit_gasto', name = "edit_gasto"),
     url("^del/(?P<id>\d.*)$", 'del_gasto', name = "del_gasto"),


     url("^tipos$", 'list_tipos', name = "list_tipos"),
     url("^tipos/nuevo$", 'add_tipo', name = "add_tipo"),
     url("^tipos/edit/(?P<tipo>\d.*)$", 'edit_tipo', name = "edit_tipo"),
     url("^tipos/del/(?P<tipo>\d.*)$", 'del_tipo', name = "del_tipo"),


     url("^categorias$", 'list_categorias', name = "list_categorias"),
     url("^categorias/nuevo$", 'add_categoria', name = "add_categoria"),
     url("^categorias/edit/(?P<nombre>\w.*)$", 'edit_categoria', name = "edit_categoria"),
     url("^categorias/del/(?P<nombre>\w.*)$", 'del_categoria', name = "del_categoria"),
     
     url("^change_month/", 'change_month', name = "change_month"),

    url("^ingreso$", 'list_ingresos', name = "list_ingresos"),
    url("^ingreso/nuevo$", 'create_ingresos', name = "create_ingreso"),
    url("^ingreso/edit/(?P<id_ingreso>\d.*)", 'edit_ingreso', name = "edit_ingreso"),
    url("^ingreso/del/(?P<id_ingreso>\d.*)", 'del_ingreso', name = "del_ingreso"),
    
     url("^balance/$", 'show_balance', name = "show_balance"),
     

)
