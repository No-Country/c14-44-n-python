from django.urls import path
from . import views


app_name = 'materia'

urlpatterns = [
    path('hola/', views.hola, name='hola')
    
]