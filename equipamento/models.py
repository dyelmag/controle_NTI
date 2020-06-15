from django.db import models
from django.contrib.auth.models import User


class Marca(models.Model):

    nome = models.CharField(blank=False, unique=True, max_length=200)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    obs = models.CharField(blank=False, max_length=400)

    def __str__(self):
        return 'Nome: %s' % (self.nome)


class Conjunto(models.Model):

    identificação = models.CharField(blank=False, max_length=200)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    obs = models.CharField(blank=False, max_length=400)


class Modelo(models.Model):
    marca = models.ForeignKey(
        Marca, on_delete=models.SET_NULL, related_name='marca', blank=True, null=True)
    nome = models.CharField(blank=False, max_length=300)
    tipo = models.CharField(blank=True, max_length=100)
    descricao = models.CharField(blank=False, max_length=400)
    obs = models.CharField(blank=False, max_length=400)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Nome: %s' % (self.nome)


class Equipamento(models.Model):

    modelo = models.ForeignKey(
        Modelo, on_delete=models.SET_NULL, related_name='modelo', blank=True, null=True)
    conjunto = models.ForeignKey(
        Conjunto, on_delete=models.SET_NULL, related_name='conjunto', blank=True, null=True)
    numero_de_serie = models.CharField(blank=True, max_length=100)
    patrimonio = models.CharField(blank=True, null=True, max_length=100)
    departamento = models.CharField(blank=True, null=True, max_length=100)
    mesa = models.CharField(blank=True, null=True, max_length=50)
    ramal_proximo = models.CharField(blank=True, null=True, max_length=50)
    usuario = models.CharField(blank=True, null=True, max_length=100)
    so = models.CharField(blank=True, null=True, max_length=50)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ponto_de_rede = models.CharField(blank=True, null=True, max_length=50)
    status = models.CharField(blank=True, null=True, max_length=100)
    obs = models.CharField(blank=False, max_length=400)
