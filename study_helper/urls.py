
from django.contrib import admin
from django.urls import path, include
from study_helper import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('alumnos/', include('alumno.urls')),
    path('profesor/', include('profesor.urls'))
]

