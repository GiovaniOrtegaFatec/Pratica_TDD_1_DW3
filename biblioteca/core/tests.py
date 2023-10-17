from django.test import TestCase
from django.shortcuts import resolve_url as r
from http import HTTPStatus
from .models import LivroModel
from .forms import LivroForm


class IndexGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:index'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 2),
            ('<br>', 3),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class IndexPostTest(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('core:index'))
        self.resp2 = self.client.post(r('core:index'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.FOUND)
        self.assertEqual(self.resp2.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp2, 'index.html')


class CadastroGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:cadastro'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'cadastro.html')

    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 5),
            ('<br>', 5),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class CadastroPostOk(TestCase):
    def setUp(self):
        data = {'titulo': 'Contos de Machado de Assis',
                'editora': 'editora Brasil',}
        self.resp = self.client.post(r('core:cadastro'), data, follow=True)
        self.resp2 = self.client.post(r('core:cadastro'), data)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
        self.assertEqual(self.resp2.status_code , HTTPStatus.FOUND)

    def test_dados_persistidos(self):
        self.assertTrue(LivroModel.objects.exists())

    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 2),
            ('<br>', 3),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class CadastroPostFail(TestCase):
    def setUp(self):
        data = {'titulo': 'Livro sem editora',}
        self.resp = self.client.post(r('core:cadastro'), data)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'cadastro.html')

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)

    def test_dados_persistidos(self):
        self.assertFalse(LivroModel.objects.exists())


class ListarGet_withoutBook_Test(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:listar'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'listar.html')
    
    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 1),
            ('Nenhum livro cadastrado', 1),
            ('<br>', 2),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class ListarPost_withoutBook_Test(TestCase):
    def setUp(self):
        data = {}
        self.resp = self.client.post(r('core:listar'), data)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'detalhes.html')
    
    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 1),
            ('Nenhum livro cadastrado', 1),
            ('<br>', 2),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class ListarGet_OneBook_Test(TestCase):
    def setUp(self):
        self.livro = LivroModel(
            titulo='Contos de Machado de Assis',
            editora='editora Brasil',)
        self.livro.save()
        self.resp = self.client.get(r('core:listar'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'listar.html')
    
    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 4),
            ('Contos de Machado de Assis', 1),
            ('<br>', 2),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class ListarPost_OneBook_Test(TestCase):
    def setUp(self):
        self.livro = LivroModel(
            titulo='Contos de Machado de Assis',
            editora='editora Brasil',)
        self.livro.save()
        data = {'livro_id': self.livro.pk}
        self.resp = self.client.post(r('core:listar'), data)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'detalhes.html')
    
    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 1),
            ('Contos de Machado de Assis', 1),
            ('<br>', 6),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class LivroModelModelTest(TestCase):
    def setUp(self):
        self.livro = LivroModel(
            titulo='Contos de Machado de Assis',
            editora='editora Brasil',)
        self.livro.save()

    def test_created(self):
        self.assertTrue(LivroModel.objects.exists())


class LivroFormTest(TestCase):
    def test_fields_in_form(self):
        form = LivroForm()
        expected = ['titulo', 'editora']
        self.assertSequenceEqual(expected, list(form.fields))
    
    def test_form_all_OK(self):
        dados = dict(titulo='Contos do Machado de Assis', editora='Editora Brasil')
        form = LivroForm(dados)
        errors = form.errors
        self.assertEqual({}, errors)
        
    def test_form_without_data_1(self):
        dados = dict(titulo='Contos do Machado de Assis')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['editora']
        msg = 'Informe a editora do livro.'
        self.assertEqual([msg], errors_list)

    def test_form_without_data_2(self):
        dados = dict(editora='Editora Brasil')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['titulo']
        msg = 'Informe o título do livro.'
        self.assertEqual([msg], errors_list)
    
    def test_form_less_than_10_character_1(self):
        dados = dict(titulo='123', editora='Editora Brasil')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['titulo']
        msg = 'Deve ter pelo menos dez caracteres'
        self.assertEqual([msg], errors_list)
    
    def test_form_less_than_10_character_2(self):
        dados = dict(titulo='Contos do Machado de Assis', editora='123')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['editora']
        msg = 'Deve ter pelo menos dez caracteres'
        self.assertEqual([msg], errors_list)

