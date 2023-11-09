from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from home.views import Home, Acerca, Contacto
from profesor.views import listar_profesores
from materia.views import Materias,registrarCurso
from aula_virtual.views import Chat, ChatInternoAula

#from materia.views import views
#from aula_virtual.views import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name="Home"),
    path('about.html', Acerca, name="Acerca"),
    path('trainers.html', listar_profesores, name="Profesor"),
    path('courses.html', Materias, name="Cursos"),
    path('chat.html', Chat, name="Chat"),
    path('contact.html', Contacto, name="Contacto"),
    path('registrarCurso/', registrarCurso, name="registrarCurso"),
    path('chat_interno_aula.html/', ChatInternoAula, name="Chat_interno_aula"),
    path('alumno/', include(('alumno.urls', 'alumno'), namespace='alumno')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
