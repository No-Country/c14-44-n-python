from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Profesor(User):
    documento= models.CharField(max_length=100, unique=True)
    phone_number = models.IntegerField("Número de Teléfono")
    phone_code = models.IntegerField("Código de Teléfono")
    biografia = models.TextField(null=True)
    foto=models.ImageField(upload_to="media/profesores", null=True, blank=True)
    materia= models.CharField(max_length=100, null=True)
    precio=models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
