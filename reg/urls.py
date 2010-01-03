from django.conf.urls.defaults import *
urlpatterns = patterns('',
    (r'^$','django.views.generic.simple.redirect_to',{'url':'prelogin/'}),
)
urlpatterns += patterns('misgastos.reg.views',
    url('prelogin/$', 'prelogin', name="prelogin"),
    url('login/$', 'login', name="login"),
)