from django.http import HttpResponse
from django.shortcuts import render
#############_______ Esto lo importo para poder hacer un CRUD mas Facil con django_______###############

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from aula_virtual.models import AulaVirtual

#############_______ Esto lo importo para poder hacer un CRUD mas Facil con django_______###############

# Create your views here.
def Chat(request):
    lista = AulaVirtual.objects.all()
    
    return render(request, "chat.html", {'lista':lista})

def ChatInternoAula(request):
    
    return render(request, "chat_interno_aula.html")


    
   
#######################################################
#-------------------CRUD---------------------------#   
#######################################################
 
#Lista de cursos:
class AulaVirtualList(ListView):
    model = AulaVirtual    
    template_name='/chat.html'

#Detalle del curso:
class AulaVirtualDetail(DetailView):
    model = AulaVirtual    
    template_name='/chat-detail.html'

#Actualizar Cursos
class AulaVirtualUpdate(UpdateView):
    model = AulaVirtual    
    success_url = '/aula/virtual'
    fields = ['nombre', 'fecha']

#Eliminar curso    
class AulaVirtualDelete(DeleteView):
    model = AulaVirtual    
    success_url = '/aula/virtual'
    
#Crear curso    
class AulaVirtualCreate(CreateView):
    model = AulaVirtual    
    success_url = '/aula/virtual'
    fields = ['nombre', 'fecha']