
from django.db import models


class AulaVirtual(models.Model):
    id_alumno = models.ForeignKey("alumno.Alumno", on_delete=models.CASCADE)
    id_profesor = models.ForeignKey("profesor.Profesor", on_delete=models.CASCADE)
    #id_materia = models.ForeignKey("materia.Materia", on_delete=models.CASCADE)
    fecha = models.DateField()
    
    
    