from django.db import models

class Livros(models.Model):
    nome_livro = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    quantidade_paginas = models.IntegerField()
    nome_autor = models.CharField(max_length=100)
    nome_editora = models.CharField(max_length=100)
    preco = models.FloatField(default=0.0)

def __str__(self):
    return self.nome_livro
