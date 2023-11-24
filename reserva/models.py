from django.db import models
from users.models import User
from instrumento.models import Instrumento

# Create your models here.

class Reserva (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE)
    data_reserva = models.DateField()
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('negado', 'Negado'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente', null=True, blank=True)

    def __str__(self):
        return f"{self.user} reservou {self.instrumento.nome} em {self.data_reserva}"
    