from django.db import models
from users.models import User

# Create your models here.

class Perfil (models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    cpf = models.CharField(blank=True, max_length=255)
    nome = models.CharField(blank=True,max_length=255)