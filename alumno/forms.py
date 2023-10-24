from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Alumno

class AlumnoRegistrationForm(UserCreationForm):
    phone_number = forms.IntegerField(label="Número de Teléfono", max_value=999999999999999)
    phone_code = forms.IntegerField(label="Código de Área", max_value=999)
    
    class Meta:
        model = Alumno
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_code', 'phone_number', 'password1', 'password2']