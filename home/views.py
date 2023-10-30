from django.shortcuts import render
from django.http import HttpResponse
#from . import models

# Create your views here.
def Home(request):
    return render(request, "index.html")

def Acerca(request):
    return render(request, "about.html")

def Contacto(request):
    return render(request, "contact.html")