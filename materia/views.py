from django.shortcuts import render, redirect
from .models import Materia

def Materias(request):
    cursosListados = Materia.objects.all()
    #return render(request, "courses.html", {"cursos": cursosListados})
    contexto = {"cursos":cursosListados}
    return render (request, "courses.html",contexto)

def registrarCurso(request):
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']

    curso = Materia.objects.create(nombre=nombre, descripcion=descripcion)
    #messages.success(request, '¡Curso registrado!')
    #return redirect('/')
    return redirect(request.META['HTTP_REFERER'])