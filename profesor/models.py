from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Profesor(User):
    documento= models.CharField(max_length=100, unique=True)
    phone_number = models.IntegerField("Número de Teléfono")
    phone_code = models.IntegerField("Código de Teléfono")
    biografia = models.TextField(null=True, blank=True)
    #usuario = models.CharField(max_length=15)
    #password = models.CharField(max_length=15)
    #valoracion = models.ForeignKey(RankingProfesor, on_delete=models.CASCADE)
