from django.db import models

class Produto(models.Model):
    descricao = models.CharField(max_length=50)
    quantidade = models.CharField(max_length=50)
    valorUnitario = models.CharField(max_length=11)

    def __str__(self):
        return self.descricao
