from django.db import models

# Create your models here.
class Pessoa(models.Model):
    pessoa_id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)
    email=models.EmailField(max_length=200)

    def __str__(self) -> str:
        return self.nome
    