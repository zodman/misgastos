from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.views import password_change, password_change_done
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect


def logout(request):
    return logout_then_login(request)

def changepass(request):
    return password_change(request)

##def register_user(request):
##    if request.POST:
##        fuser = UserCreationForm(request.POST)
##        if fuser.is_valid():
##            fuser.save()
##            return HttpResponseRedirect(reverse("index"))
##        else:


def prelogin(request):
    if request.method == "POST":
        return login(request)
    else:
        return direct_to_template( request, template="registration/login.html",
                extra_context = dict(
                        form_create = UserCreationForm(),
                        form = AuthenticationForm()
                ))