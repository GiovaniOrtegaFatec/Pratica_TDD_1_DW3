# Prática TDD

Desafio técnico para os alunos da disciplina "Desenvolvimento Web 3" e "Qualidade e Teste de Software"


```console
git clone https://github.com/orlandosaraivajr/Desenvolvimento_web_3.git
cd Desenvolvimento_web_3/
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
cd biblioteca/
python manage.py test
coverage run --source='.' manage.py test 
coverage html
python manage.py runserver
```
