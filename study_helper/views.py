from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

def index(request):
    return HttpResponse("Study-Helper | Hola Mundo!")