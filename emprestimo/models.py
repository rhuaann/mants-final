from django.db import models
from users.models import User
from instrumento.models import Instrumento

# Create your models here.

class Emprestimo (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()
    STATUS_CHOICES = (
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('pendente', 'Pendente'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return f"Empréstimo de {self.instrumento.nome} realizado em {self.data_emprestimo} por {self.user}"