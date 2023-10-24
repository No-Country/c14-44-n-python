from django.urls import path
from .views import AlumnoRegistrationView, hola, success


app_name = 'alumnos'

urlpatterns = [
    path('hola/', hola, name='hola'),
    path('signup/', AlumnoRegistrationView.as_view(), name='signup'),
    path('success/', success, name='success'),
    
]