from django.shortcuts import render
from profesor.models import Profesor

# Create your views here.
def listar_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, "trainers.html",{"profesores":profesores})