# To Do List API
![Capa](https://user-images.githubusercontent.com/86068797/209870423-3ba162d9-78d9-4e51-b5e2-c2ccd6424508.png)

<p align="center">
 <a href="#descrição-do-projeto-">Descrição</a> •
 <a href="#estrutura-de-pastas-%EF%B8%8F">Pastas</a> • 
 <a href="#demonstração-da-aplicação-">Demonstração</a> • 
 <a href="#funcionalidades-%EF%B8%8F">Funcionalidades</a> • 
 <a href="#status-do-projeto-">Status</a> • 
 <a href="#como-rodar-a-aplicação-">Como Rodar</a> • 
 <a href="#tecnologias-%EF%B8%8F">Tecnologias</a> • 
 <a href="#desenvolvedor-octocat">Desenvolvedor</a>
</p>

## Descrição do Projeto 📋
Esta é uma API desenvolvida com o Django Rest Framework, a qual funciona como uma lista de tarefas (to do list).
Nesse viés, tal API possibilita a criação de tarefas com os seguintes campos: título, descrição, data de
conclusão e status de conclusão. Além de criar, também é possível listar, atualizar e deletar tarefas.

<div align="center">
    <img alt="Badge com a versão utilizada do Python" src="https://img.shields.io/static/v1?label=PYTHON&message=3.9.9&color=blue&style=for-the-badge&logo=Python"/>
    <img alt="Badge com a versão utilizada do Django" src="https://img.shields.io/static/v1?label=DJANGO&message=4.0.1&color=brightgreen&style=for-the-badge&logo=DJANGO&logoColor=green"/>
    <img alt="Badge com a versão utilizada do Django" src="https://img.shields.io/static/v1?label=D.R.F&message=3.14.0&color=red&style=for-the-badge&logo=DJANGO&logoColor=red"/>
</div>

## Estrutura de Pastas 🗂️
* Raíz

    ├── config <br>
    ├── to_do_list <br>
        &emsp;&emsp; └── migrations <br>
    ├ manage.py <br>
    ├ README.md <br>
    ├ requirements.txt <br>

Na pasta raiz, há três arquivos **principais**:

* **README.md**: guia sobre os aspectos do projeto
* **manage.py**: *script* que auxilia na gestão da API
* **requirements.txt**: requisitos para rodar a aplicação

Ademais, há duas pastas, as quais estão organizadas do seguinte modo:

* **config/**: pasta do *django project*, responsável por organizar todos os arquivos de configuração do projeto;
* **to_do_list/**: pasta do *django app*, responsável por organizar os arquivos relacionados ao aplicativo das tarefas.

## Demonstração da Aplicação 💻
> Dados para a inclusão de uma tarefa - post

<img src="https://user-images.githubusercontent.com/86068797/209858395-8e87eb76-bf26-48c2-a279-6f0c7a55fe6a.png" alt="imagem com o conteúdo necessário para a inclusão de uma tarefa" title="Conteúdo necessário para a inclusão de uma tarefa">

> Listagem das tarefas - get /tarefas/

<img src="https://user-images.githubusercontent.com/86068797/209858766-75770773-f536-4f9d-8852-956e52d6ef84.png" alt="imagem com o conteúdo listado a partir do método get" title="Listagem das tarefas via GET">

## Funcionalidades ⚙️

- [x] Criar tarefas com os campos:
  - [x] Título
  - [x] Data de Conclusão
  - [x] Status da Tarefa
  - [x] Descrição
- [x] Manipular as tarefas criadas:
  - [x] Listar todas
  - [x] Listar por ID
  - [x] Atualizar
  - [x] Deletar

## Status do Projeto 🔔
#### 🚧 Em Aprimoramento 🚧 

## Como Rodar a Aplicação 🚀

### Pré-requisitos 📦
Antes de começar, é preciso que você tenha as seguintes ferramentas instaladas em sua máquina:

[Git](https://git-scm.com/), [Python](https://www.python.org/downloads/release/python-390/).

Além disso, é interessante que você tenha um editor para trabalhar com o código. Recomendo o uso do [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows) ou do [VSCode](https://code.visualstudio.com/)

### Rodando a Aplicação ▶
```bash
# No terminal, clone este repositório:
git clone <https://github.com/VictorGM01/to_do_api>

# Acesse a pasta do projeto
cd to_do_api

# Crie e ative um ambiente virtual
python -m venv .venv
.venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Defina as variáveis de ambiente
# Crie, na raíz do projeto, um arquivo chamado .env
# Neste arquivo, defina as seguintes variáveis:
SECRET_KEY="cole-sua-chave-aqui"
DEBUG="1"

# Realize as migrações
python manage.py migrate

# Crie um usuário admin
python manage.py createsuperuser

# Rode o servidor
python manage.py runserver
```

### Rodando os Testes da API ✅
```bash
# Após seguir os passos anteriores, certifique-se de estar na raíz do projeto
cd to_do_api

# Para rodar todos os testes, execute:
python manage.py test

# Para rodar somente os testes das tarefas, execute:
python manage.py test to_do_list

# Para rodar um método em específico, execute:
python manage.py test to_do_list.tests.TestTarefas.digite_o_nome_do_metodo_aqui
# Ex.: python manage.py test to_do_list.tests.TestTarefas.test_deve_retornar_status_code_200_no_metodo_get
```

## Tecnologias 🛠️
As seguintes ferramentas foram usadas na construção do projeto:

* [**Python**](https://www.python.org/downloads/release/python-399/)
* [**Django**](https://www.djangoproject.com/)
* [**Django Rest Framework**](https://www.django-rest-framework.org/)
* [**SQLite**](https://www.sqlite.org/index.html)
* [**Fly**](https://fly.io/docs/)
* [**Jazzmin**](https://django-jazzmin.readthedocs.io/)

## Desenvolvedor :octocat:
[<img src="https://avatars.githubusercontent.com/u/86068797?s=400&u=043c0b1479770ac997f0cf5a31c986a2815ce810&v=4" width=100><br><sub> <strong>Victor G. Marques</strong> </sub>](https://github.com/VictorGM01)

[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/victor-marques-profile)](https://www.linkedin.com/in/victor-marques-profile/)
[![Gmail Badge](https://img.shields.io/badge/-Gmail-red?style=flat-square&logo=Gmail&logoColor=white&link=https://www.linkedin.com/in/victor-marques-profile)](mailto:victormarques8801@gmail.com")

Feito com ❤️ por Victor Marques 🖥️🔬