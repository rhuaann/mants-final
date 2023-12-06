from django.db import models

# Create your models here.

class Instrumento (models.Model):
    nome = models.CharField(max_length=100)
    TIPO_CHOICES = (
        ('sopro', 'Sopro'),
        ('cordas', 'Cordas'),
        ('percussão', 'Percussão'),
    )
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    STATUS_CHOICES = (
        ('disponivel', 'Disponível'),
        ('reservado', 'Reservado'),
        ('emprestado', 'Emprestado'),
        ('defeito', 'Com defeito'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='disponivel')


    def __str__(self):
        return f"{self.nome} | {self.status}"

    # def has_defeito(self):
    #     return self.defeito

    # def registrar_defeito(self):
    #     self.defeito = True
    #     self.save()

    # def resolver_defeito(self):
    #     self.defeito = False
    #     self.save()

        