from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Alumno
from .forms import AlumnoRegistrationForm
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse

def hola(request):
    return HttpResponse("Hola Alumno!")

def success(request):
    return HttpResponse("Exito!")
    
class AlumnoRegistrationView(CreateView):
    model = Alumno
    form_class = AlumnoRegistrationForm
    template_name = 'signup.html'  # Crea un template de registro
    success_url = reverse_lazy('alumnos:success')
