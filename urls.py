from django.conf.urls.defaults import *
from misgastos.settings import MEDIA_ROOT

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^gasto/', include('misgastos.gastos.urls')),
    (r'^$','django.views.generic.simple.direct_to_template',{'template':'principal.html'}),
   # (r'^accounts/', include("misgastos.reg.urls")),
    (r'^accounts/', include('registration.backends.default.urls')),



    (r'^admin/', include(admin.site.urls)),
    (r'^static/(.*)','django.views.static.serve', {'document_root': MEDIA_ROOT, 'show_indexes': True})
)
