from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=40)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome
