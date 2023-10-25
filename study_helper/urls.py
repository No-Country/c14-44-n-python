
from django.contrib import admin
from django.urls import path, include
from study_helper.views import Index


urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', Index.as_view(), name='index'),
    path('alumnos/', include('alumno.urls'))
=======
    path('', views.index),
    path('alumnos/', include('alumno.urls')),
    path('profesor/', include('profesor.urls')),
    path('materia/', include('materia.urls')),
    path('aula_virtual/', include('aula_virtual.urls')),
>>>>>>> 14822ed5dc4ac050e84dab0e358ed15285ee1a02
]

