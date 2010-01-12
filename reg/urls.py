from django.conf.urls.defaults import *
urlpatterns = patterns('',
    (r'^$','django.views.generic.simple.redirect_to',{'url':'prelogin/'}),
)
urlpatterns += patterns('misgastos.reg.views',
    url('prelogin/$', 'prelogin', name="prelogin"),
    url('login/$', 'login', name="login"),
    url('logout/$','logout', name="logout"),
    url('password_change/$','changepass', name="changepass"),
    url('password_change_done/$','password_change_done', name="password_change_done"),
)