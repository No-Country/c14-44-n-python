from django.db import models
from django.contrib.auth.models import User

class Profesor(User):
    documento= models.CharField(max_length=100, unique=True)
    phone_number = models.IntegerField("Número de Teléfono", max_length=15, default=0)
    phone_code = models.IntegerField("Código de Teléfono", max_length=3, default=0)
    #valoracion = models.ForeignKey(RankingProfesor, on_delete=models.CASCADE)
