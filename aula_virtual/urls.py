from django.urls import path
from aula_virtual import views
from . import views


app_name = 'aula_virtual'

urlpatterns = [
    #path('prueba/', views.Chat, name='Chat'),    
    path('aula/virtual', views.AulaVirtualList.as_view(), name = 'List'),
    path('detalleAula/<pk>/', views.AulaVirtualDetail.as_view(), name='Detail'),
    path('crearAula/', views.AulaVirtualCreate.as_view(), name='New'),
    path('actualizarAula/<pk>/', views.AulaVirtualUpdate.as_view(), name='Edit'),
    path('eliminarAula/<pk>/', views.AulaVirtualDelete.as_view(), name='Delete'),
    
    
]