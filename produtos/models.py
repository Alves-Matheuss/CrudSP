from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    unidade_medida = models.CharField(max_length=3, choices=[
        ('kg', 'Kilograma'),
        ('g', 'Grama'),
        ('un', 'Unidade'),
    ])
    estoque = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
