from django.contrib.auth.views import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.simple import direct_to_template

def prelogin(request):
    if request.method == "POST":
        return login(request)
    else:
        return direct_to_template( request, template="registration/login.html",
                extra_context = dict(
                        form_create = UserCreationForm(),
                        form = AuthenticationForm()
                    )
             )