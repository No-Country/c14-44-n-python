from django.db import models
from django.contrib.auth.models import User

class Profesor(User):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento= models.CharField(max_length=100, unique=True)
    rol = models.ForeignKey(AulaVirtual, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    valoracion = models.ForeignKey(RankingProfesor, on_delete=models.CASCADE)
