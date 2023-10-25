from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Profesor(User):
    #nombre = models.CharField(max_length=100)
    #apellido = models.CharField(max_length=100)
    documento= models.CharField(max_length=100, unique=True)
    #rol = models.ForeignKey(AulaVirtual, on_delete=models.CASCADE)
    #email = models.EmailField(unique=True)
    #telefono = models.CharField(max_length=20)
    phone_number = models.IntegerField("Número de Teléfono", default=1000000000, validators = [
        MaxValueValidator(999999999999999),
        MinValueValidator(1000000000)
    ])
    phone_code = models.IntegerField("Código de Teléfono", default=10, validators = [
        MaxValueValidator(999),
        MinValueValidator(10)
    ])
    #valoracion = models.ForeignKey(RankingProfesor, on_delete=models.CASCADE)
