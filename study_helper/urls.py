from django.contrib import admin
from django.urls import path, include
from home.views import Home, Acerca, Contacto
from profesor.views import Profesor
from materia.views import Materias
from aula_virtual.views import Chat

#from materia.views import views
#from aula_virtual.views import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name="Home"),
    path('about.html', Acerca, name="Acerca"),
    path('trainers.html', Profesor, name="Profesor"),
    path('courses.html', Materias, name="Cursos"),
    path('chat.html', Chat, name="Chat"),
    path('contact.html', Contacto, name="Contacto"),
]


