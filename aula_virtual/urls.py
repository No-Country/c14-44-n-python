from django.urls import path
from . import views


app_name = 'aula_virtual'

urlpatterns = [
    path('prueba/', views.prueba, name='prueba')
    
]