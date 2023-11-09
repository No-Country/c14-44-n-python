from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Alumno

class AlumnoRegistrationForm(UserCreationForm):
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput,
        help_text="Reingrese su contraseña para confirmar",
    )

    class Meta:
        model = Alumno
        fields = ['username', 'first_name', 'password1', 'password2', 'phone_number', 'email', 'tipo_documento', 'num_documento']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2
        
    def save(self, commit=True):
        user = super(AlumnoRegistrationForm, self).save(commit=False)
        if commit:
            user.save()
            return user
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))