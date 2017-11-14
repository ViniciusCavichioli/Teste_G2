from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from django.http import HttpResponse
from lpc_evento.models import *
from lpc_evento.serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class FrequenciaDiaViewSet(viewsets.ModelViewSet):
    queryset = FrequenciaDia.objects.all()
    serializer_class = FrequenciaDiaSerializer
