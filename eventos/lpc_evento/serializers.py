from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from lpc_evento.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UserSerializer(many = False)
    class Meta:
        model = Pessoa
        fields = ('nome', 'email', 'sexo', 'idade', 'situacaoFuncional', 'usuario', 'url')

    #def create(self, dados):
    #    dados_usuario = dados.pop('usuario')
    #    U = User.objects.create(**dados_usuario)
    #    P = Pessoa.objects.create(usuario = U, **dados)
    #    return P

class FrequenciaDiaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FrequenciaDia
        fields = ('HoraEntrada','HoraSaidaAlmoco','HoraRetornoAlmoco', 'HoraSaida',
         'ipMaquina', 'nomeChefe', 'statusFrequencia', 'justificativa', 'funcionario', 'url' )

    #def create(self, dados):
    #    dados_pessoa = dados.pop('funcionario')
    #    P = Pessoa.objects.get(nome = dados_pessoa)
    #    F = FrequenciaDia.objects.create(funcionario = P, **dados)
    #    return F
