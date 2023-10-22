from django.db import models

class Materia (models.Model):
    nombre: models.CharField(max_length=100)
    descripcion: models.TextField()