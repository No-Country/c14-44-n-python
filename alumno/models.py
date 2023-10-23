from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Alumno(User):
    phone_number = models.IntegerField("Número de Teléfono", max_length=15, default=0)
    code = models.IntegerField("código", max_length=3, default=0)
    
