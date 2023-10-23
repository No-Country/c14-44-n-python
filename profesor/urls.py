from django.urls import path
from . import views

app_name = 'profesor'

urlpatterns = [
    path('prueba/', views.prueba, name='prueba'),
]