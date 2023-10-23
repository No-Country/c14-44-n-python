from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
# Create your views here.

def hola(request):
    return HttpResponse("Materias!!")
