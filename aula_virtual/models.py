
# Create your models here.
from django.db import models


class AulaVirtual(models.Model):    
    id_alumno = models.ForeignKey("alumno.Alumno", on_delete=models.CASCADE)
    id_profesor = models.ForeignKey("profesor.Profesor", on_delete=models.CASCADE)   
    nombre = models.CharField("nombre", max_length=50)
    material = models.CharField('material',max_length=10000)
    fecha = models.DateField("fecha_de_clase",)
    def __str__(self):
        return f'Aula: {self.nombre} - Fecha: {self.fecha}'
    
    
    