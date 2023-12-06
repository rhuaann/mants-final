from django.db import models
from defeito.models import Defeito
from users.models import User

# Create your models here.

class Manutencao(models.Model):
    defeito = models.ForeignKey(Defeito, on_delete=models.CASCADE)
    tecnico_responsavel = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    descricao_servico = models.TextField()
    data_inicio = models.DateField()
    data_conclusao = models.DateField(null=True)

    def __str__(self):
        return f"{self.defeito.instrumento.nome} | {self.data_inicio} | {self.data_conclusao} | {self.tecnico_responsavel}"