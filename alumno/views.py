from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import AlumnoRegistrationForm
from django.contrib.auth import login, authenticate
from .models import Alumno
from .forms import LoginForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView


'''class LoginAlumno(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm'''

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Haz iniciado sesión como {username}.")
                return render(request, "index.html")
            else:
                messages.error(request,"Usario o contraseña no válidos.")
        else:
            messages.error(request,"Usario o contraseña no válidos.")
    form = AuthenticationForm()
    messages.error(request,"Usario o contraseña no válidos.")
    return render(request=request, template_name="login.html", context={"login_form":form})


def signup(request):
    
    if request.method == "POST":
        formulario = AlumnoRegistrationForm(request.POST)
        
        if formulario.is_valid():
            
            formulario.save()
            return render(request, "index.html")
        else:
            return render(request, "registro.html", { "form": formulario, "errors": formulario.errors})

    formulario  = AlumnoRegistrationForm()
    return render(request, "registro.html", { "form": formulario})
    
'''class SignupUsuario(CreateView):
    template_name = 'registro.html'
    model = Alumno
    form_class = AlumnoRegistrationForm
    #extra_context = {'etiqueta':'Nuevo', 'boton':'Agregar', 'nuevo_user':True}
    success_url = reverse_lazy('alumno:login')'''