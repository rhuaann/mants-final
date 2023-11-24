from django.db import models
from users.models import User

# Create your models here.

class Perfil (models.Model):
    cpf = models.CharField(max_length=50, null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)