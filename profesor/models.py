from django.db import models
from django.contrib.auth.models import User

class Profesor(User):
    #nombre = models.CharField(max_length=100)
    #apellido = models.CharField(max_length=100)
    documento= models.CharField(max_length=100, unique=True)
<<<<<<< HEAD
    #rol = models.ForeignKey(AulaVirtual, on_delete=models.CASCADE)
    #email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
=======
    phone_number = models.IntegerField("Número de Teléfono", max_length=15)
    phone_code = models.IntegerField("Código de Teléfono", max_length=3)
>>>>>>> 14822ed5dc4ac050e84dab0e358ed15285ee1a02
    #valoracion = models.ForeignKey(RankingProfesor, on_delete=models.CASCADE)
