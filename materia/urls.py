from django.urls import path
from materia import views
#app_name = 'materia'

urlpatterns = [
   path('courses/',views.Materias),
   path('registrarCurso/', views.registrarCurso),
]
# path('hola/', views.hola, name='hola')