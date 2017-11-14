from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length = 128)
    email = models.CharField(max_length = 100)
    sexo = models.CharField(max_length=10)
    idade = models.IntegerField()
    situacao_choice = (
        ('ST','Estagiario'),
        ('SR', 'Servidor')
    )
    situacaoFuncional = models.CharField(max_length = 15, choices = situacao_choice)
    usuario = models.ForeignKey(User, null=True, blank=False)

    def __str__(self):
        return self.nome + self.situacaoFuncional

class FrequenciaDia(models.Model):
    HoraEntrada = models.DateTimeField()
    HoraSaidaAlmoco = models.DateTimeField()
    HoraRetornoAlmoco = models.DateTimeField()
    HoraSaida = models.DateTimeField()
    ipMaquina = models.CharField(max_length = 15)
    nomeChefe = models.CharField(max_length = 128, null = True, blank = False)
    status_choice = (
        ('IN','INCONSISTENTE'),
        ('CN','CONSISTENTE')
    )
    statusFrequencia = models.CharField(max_length = 2, choices = status_choice)
    justificativa = models.TextField(max_length = 200, null = True, blank = True)

    funcionario = models.ForeignKey(Pessoa, related_name = 'Funcionario', null = True, blank = False)

    def __str__(self):
        return '{}'.format(self.funcionario)
