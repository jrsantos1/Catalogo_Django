from django.db import models
from datetime import datetime

# Create your models here.

#criando modelo para enviar ao banco de dados

class Moto(models.Model):
    nome = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)
    preco = models.FloatField()
    ano_lancamento = models.IntegerField()
    data_inclusao = models.DateTimeField(default=datetime.now, blank=True)