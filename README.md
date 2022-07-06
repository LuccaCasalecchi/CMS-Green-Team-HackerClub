## CMS Green Team Hacker Club




# Run project

Certifique-se de ter o Python instaldo em sua máquina local para clonar o repositório.

## Instruções para rodar o projeto localmente:

- Crie um diretório e acesse ele pelo seu terminal (`cd <diretório>`)
- `git clone https://github.com/LuccaCasalecchi/CMS-Green-Team-HackerClub.git`
- Navegue até o diretório do `CMS-Green-Team-HackerClub`
- Crie um ambiente virtual, caso esteja utilizando Windows o comando é: `python3 -m venv venv`
- `venv\Scripts\activate`
- `pip freeze > requirements.txt`
- `pip install Django`
- `python manage.py migrate`
- `python manage.py runserver`

### Após esse processo, abra o projeto em ```localhost:8000```
