from django.db import models

# Create your models here.

class Fornecedor(models.Model):
    nome = models.CharField(max_length=40)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    cnpj = models.CharField(max_length=20)

    def __str__(self):
        return self.nome