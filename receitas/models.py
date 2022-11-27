from django.db import models
from datetime import datetime
from pessoa.models import PessoaModel

# Create your models here.

class ReceitaModel(models.Model):
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    pessoa = models.ForeignKey(PessoaModel, on_delete=models.CASCADE)
    imagem_receita = models.ImageField(upload_to="fotos/%d/%m/%Y", blank=True)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_receita
