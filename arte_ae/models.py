from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Evento(models.Model):
    nome = models.CharField(max_length=300)
    logradouro = models.CharField(max_length=300)
    numero = models.CharField(max_length=4)
    cep = models.CharField(max_length=50)
    bairro = models.CharField(max_length=300)
    localidade = models.CharField(max_length=300)
    uf = models.CharField(max_length=2)
    data = models.DateField()
    horario = models.TimeField()
    imagem = models.ImageField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.nome