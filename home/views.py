from django.shortcuts import render
from django.http import HttpResponse
from profesor.models import Profesor
#from . import models

# Create your views here.
def Home(request):
    profesores = Profesor.objects.all().order_by('-id')[:6]
    return render(request, "index.html",{"profesores":profesores})

def Acerca(request):
    return render(request, "about.html")

def Contacto(request):
    return render(request, "contact.html")