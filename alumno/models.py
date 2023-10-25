from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Alumno(User):
    phone_number = models.IntegerField("Número de Teléfono", default=1000000000, validators = [
        MaxValueValidator(999999999999999),
        MinValueValidator(1000000000)
    ])
    phone_code = models.IntegerField("Código de Teléfono", default=10, validators = [
        MaxValueValidator(999),
        MinValueValidator(10)
    ])
    
    