from django import forms
from django.core.exceptions import ValidationError
from core.models import LivroModel


def validate_titulo(titulo):
    if len(titulo) < 3:
        raise ValidationError('O título do livro deve conter pelo menos 03 (três) caracteres')

def validate_editora(editora):
    if len(editora) < 3:
        raise ValidationError('O nome da Editora deve conter pelo menos 03 (três) caracteres')
    
def validate_autor(autor):
    if len(autor) < 10:
        raise ValidationError('O nome do autor deve conter pelo menos 10 (dez) caracteres')
    
def validate_isbn(isbn):
    if not (isbn.isdigit() and len(isbn) == 13):
        raise ValidationError('O código ISBN deve conter exatamente 13 (treze) caracteres numéricos')
    
def validate_num_pagina(num_pagina):
    if not (1 <= len(num_pagina) <= 3) or not num_pagina.isdigit():
        raise ValidationError('O número de páginas deve conter entre 01 (um) a 03 (três) caracteres numéricos')
    
def validate_ano_livro(ano_livro):
    if not (ano_livro.isdigit() and len(ano_livro) == 4):
        raise ValidationError('O ano do livro deve conter exatamente 04 (quatro) caracteres numéricos')

class LivroForm(forms.ModelForm):

    class Meta:
        model = LivroModel
        fields = ['titulo', 'editora', 'autor', 'isbn', 'num_pagina', 'ano_livro']
        error_messages = {
            'titulo': {
                'required': ("Informe o título do livro."),
            },
            'editora': {
                'required': ("Informe a editora do livro."),
            },
            'autor': {
                'required': ("Informe o autor do livro."),
            },
            'isbn': {
                'required': ("Informe o código ISBN do livro."),
            },
            'num_pagina': {
                'required': ("Informe o número de páginas do livro."),
            },
            'ano_livro': {
                'required': ("Informe o ano do livro."),
            },
        }

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        validate_titulo(titulo)
        return titulo

    def clean_editora(self):
        editora = self.cleaned_data['editora']
        validate_editora(editora)
        return editora
    
    def clean_autor(self):
        autor = self.cleaned_data['autor']
        validate_autor(autor)
        return autor
    
    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        validate_isbn(isbn)
        return isbn
    
    def clean_num_pagina(self):
        num_pagina = self.cleaned_data['num_pagina']
        validate_num_pagina(num_pagina)
        return num_pagina
    
    def clean_ano_livro(self):
        ano_livro = self.cleaned_data['ano_livro']
        validate_ano_livro(ano_livro)
        return ano_livro

    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data

