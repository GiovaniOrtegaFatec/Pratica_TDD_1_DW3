# Prática TDD

Desafio técnico para os alunos da disciplina "Desenvolvimento Web 3" e "Qualidade e Teste de Software"


```console
git clone https://github.com/orlandosaraivajr/Pratica_TDD_1.git
cd Pratica_TDD_1/
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
cd biblioteca/
python manage.py migrate
python manage.py test
coverage run --source='.' manage.py test 
coverage html
python manage.py runserver
```
