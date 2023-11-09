from django.urls import path
from home import views

urlpatterns = [
    #path('prueba/', views.prueba, name='prueba'),
    path('index.html', views.Inicio, name="Inicio"),
]