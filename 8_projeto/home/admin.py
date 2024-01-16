from django.contrib import admin
from .models import Livros

class ListLivro(admin.ModelAdmin):
    list_display = ('nome_livro', 'ano_publicacao', 'quantidade_paginas', 'nome_autor', 'nome_editora', 'preco' )
    
    
admin.site.register(Livros, ListLivro)
