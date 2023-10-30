from django.urls import path
from . import views

urlpatterns = [
    #path('prueba/', views.prueba, name='prueba'),
    path('trainers.html', views.Profesor, name="Profesor"),
]