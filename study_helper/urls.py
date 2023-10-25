
from django.contrib import admin
from django.urls import path, include
from study_helper.views import Index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('alumnos/', include('alumno.urls')),
    path('profesor/', include('profesor.urls')),
    path('materia/', include('materia.urls')),
    path('aula_virtual/', include('aula_virtual.urls')),
]



