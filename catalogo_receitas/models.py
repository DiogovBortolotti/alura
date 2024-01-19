from django.db import models
from datetime import datetime
# Create your models here.

from pessoas.models import Pessoa

class Receita(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True)
    receita_id = models.IntegerField(primary_key=True)
    nome_receita = models.CharField(max_length=150)
    data = models.DateTimeField(default=datetime.now(), blank=True, null=True)
    modo_preparo = models.CharField(max_length=250)
    tempo_preparo = models.CharField(max_length=250)
    #foto_receita = 
    ingredientes = models.CharField(max_length=250)
    rendimento = models.CharField(max_length=120)
    categoria = models.CharField(max_length=120)
