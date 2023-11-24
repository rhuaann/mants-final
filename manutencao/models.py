from django.db import models
from instrumento.models import Instrumento
from users.models import User

# Create your models here.

class Manutencao(models.Model):
    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE)
    tecnico_responsavel = models.CharField(max_length=100)
    descricao_servico = models.TextField()
    data_inicio = models.DateField()
    data_conclusao = models.DateField()

    def __str__(self):
        return f"Manutenção em {self.instrumento.nome} resolvido em {self.data_conclusao} por {self.tecnico_responsavel}"

    def resolver_defeito_associado(self):
        if self.instrumento.defeito:
            self.instrumento.resolver_defeito()