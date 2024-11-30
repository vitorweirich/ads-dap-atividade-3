## Projeto da Atividade Avaliativa 3

Projeto desenvolvido como parte da Atividade Avaliativa 3 (Atividade Problematizadora) do curso de **Análise e Desenvolvimento de Sistemas**, na disciplina de **Desenvolvimento de Aplicações**.

**Aluno:** Vitor Mateus Weirich

---

### Sobre o Repositório

Este repositório contém um projeto desenvolvido em Django, com as seguintes características:

- **Framework:** Django (Python)
- **Estilização:** Bootstrap
- **Banco de Dados:** MySQL
- **Funcionalidades:** CRUD básico de funcionários

Além disso, foi gravado um vídeo com um _overview_ do projeto e demonstrações de suas funcionalidades. O vídeo está disponível no [YouTube](https://youtube.com/TODO).

---

### Pré-requisitos

Antes de rodar o projeto, certifique-se de ter os seguintes requisitos instalados:

- **Python** (versão 3.10.0 ou superior, utilizada no desenvolvimento e testes)
- **Docker** e **Docker Compose** (para rodar o MySQL)
  - Caso prefira, você pode instalar o MySQL localmente ou alterar a configuração para usar o SQLite como banco de dados.
- **pip** (para gerenciar as dependências do Python)
- **virtualenv** (para criar um ambiente virtual para instalar as dependências)

---

### Como Rodar o Projeto

Siga os passos abaixo para rodar o projeto:

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/vitorweirich/ads-dap-atividade-3.git
   cd ads-dap-atividade-3
   ```
2. **Crie e ative um ambiente virtual com `virtualenv`:**
   ```bash
   # Criar virtual env (necessarios apenas uma vez)
   python -m virtualenv venv
   # Ativar o virtual env (caso queira desativar é só usar o comando 'dactivate' no terminal enquanto estiver com o virtual env ativo)
   venv\Scripts\activate
   ```
3. **Instale as dependências do projeto**
   ```bash
   pip install -r requirements.txt
   ```
4. **Rode as migrações do banco de dados:**
   ```bash
   docker-compose up -d
   ```
5. **Inicie o MySQL com Docker Compose:**
   ```bash
   python manage.py migrate
   ```
6. **Inicie o servidor de desenvolvimento do Django:**
   ```bash
   python manage.py runserver
   ```
7. **Acesse o projeto no navegador:** Abra http://localhost:8000/app/lista_funcionarios
