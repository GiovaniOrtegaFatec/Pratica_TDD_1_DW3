from django.db import models

class LivroModel(models.Model):
    titulo = models.CharField('Título', max_length=200)
    editora = models.CharField('editora', max_length=200)
    autor = models.CharField('Autor', max_length=200)
    isbn = models.CharField('ISBN', max_length=13)
    num_pagina = models.CharField('Páginas', max_length=3)
    ano_livro = models.CharField('Edição', max_length=4)

    def __str__(self):
        return self.titulo