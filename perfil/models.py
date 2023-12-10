from django.db import models
from users.models import User

# Create your models here.
TIPO_GENERO = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Transgênero', 'Transgênero'),
        ('Gênero Neutro', 'Gênero Neutro'),
        ('Não-binário', 'Não-binário'),
        ('Prefiro não responder', 'Prefiro não responder'),
        ('Outro', 'Outro'),
    )

class Perfil (models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(blank=True, max_length=255)
    nome = models.CharField(blank=True, max_length=255)
    foto_perfil = models.ImageField(
        upload_to='static/images/media', null=True, blank=True, default="static/images/media/user.png")
    genero = models.CharField(max_length=100, choices=TIPO_GENERO, blank=True, default="Outro")
    telefone = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return f"{self.usuario}"