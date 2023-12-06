from django.db import models
from instrumento.models import Instrumento
from users.models import User

# Create your models here.

class Defeito (models.Model):
    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE, related_name='defeitos_associados')
    relatado_por = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    descricao = models.TextField()
    data_relato = models.DateField()
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('resolvido', 'Resolvido'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return f"{self.instrumento.nome} | {self.data_relato} | {self.descricao} | {self.status} | {self.relatado_por}"
