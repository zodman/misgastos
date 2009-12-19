from django.conf.urls.defaults import *

urlpatterns = patterns('misgatos.gastos.views',

    url("^tipos/lista/$", 'list_tipos', name = "list_tipos")
)