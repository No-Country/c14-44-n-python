
from django.db import models


class AulaVirtual(models.Model):
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    fecha = models.DateField()
    