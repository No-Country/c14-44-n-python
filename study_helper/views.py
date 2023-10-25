from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.html'