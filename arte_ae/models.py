from django.db import models

# Create your models here.
class Evento(models.Model):
    cep = models.CharField(max_length=50)
    logradouro = models.CharField(max_length=300)
    bairro = models.CharField(max_length=300)
    localidade = models.CharField(max_length=300)
    uf = models.CharField(max_length=2)
    numero = models.CharField(max_length=4)
    dataHora = models.DateField()
    imagem = models.ImageField()
    nome = models.CharField(max_length=300)

    def __str__(self):
        return self.nome