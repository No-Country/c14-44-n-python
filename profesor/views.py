from django.shortcuts import render
from profesor.models import Profesor

# Create your views here.
def Profesor(request):
    return render(request, "trainers.html")