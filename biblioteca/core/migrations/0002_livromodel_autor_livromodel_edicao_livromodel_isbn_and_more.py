# Generated by Django 4.2.6 on 2023-11-02 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livromodel',
            name='autor',
            field=models.CharField(default='Desconhecido', max_length=200, verbose_name='Autor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livromodel',
            name='ano_livro',
            field=models.CharField(default='Desconhecido', max_length=4, verbose_name='Edição'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livromodel',
            name='isbn',
            field=models.CharField(default='Desconhecido', max_length=13, verbose_name='ISBN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livromodel',
            name='num_pagina',
            field=models.CharField(default='Desconhecido', max_length=3, verbose_name='Páginas'),
            preserve_default=False,
        ),
    ]