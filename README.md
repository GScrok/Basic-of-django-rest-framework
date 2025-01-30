# Cadastro de Vagas com Django REST Framework

Este é um projeto básico de **API REST** desenvolvido com **Django REST Framework (DRF)**, permitindo o cadastro de **vagas de emprego** e sua vinculação com **skills** (linguagens de programação).

O objetivo principal do projeto foi explorar e compreender o funcionamento do **ModelViewSet** no DRF, permitindo uma implementação ágil e simplificada das operações CRUD.

## **Tecnologias Utilizadas**

- **Python** 🐍
- **Django** 🦄
- **Django REST Framework** 🌍
- **Banco de Dados SQLite**
- **Gerenciador de Pacotes: UV** (com suporte para `pip` via `requirements.txt`)

## **Instalação e Execução**

### 🔹 **Usando UV (Necessário instalação)**

```bash
uv run manage.py migrate
uv run manage.py runserver
```

### 🔹 **Usando Pip**

```bash
python -m venv .venv  
.venv\Scripts\activate  
pip install -r requirements.txt  
```

```bash
python manage.py migrate  
python manage.py runserver  
```

---

## **Endpoints da API**

O projeto utiliza **ModelViewSet** para gerenciar as operações CRUD de **Vagas** e **Skills**, garantindo uma estrutura organizada e reutilizável.

### 🔹 **Vagas (`/api/jobs/`)**

| Método | Endpoint          | Descrição                     |
| ------ | ----------------- | ----------------------------- |
| GET    | `/api/jobs/`      | Lista todas as vagas          |
| POST   | `/api/jobs/`      | Cria uma nova vaga            |
| GET    | `/api/jobs/{id}/` | Obtém os detalhes de uma vaga |
| PUT    | `/api/jobs/{id}/` | Atualiza uma vaga existente   |
| DELETE | `/api/jobs/{id}/` | Remove uma vaga               |

### 🔹 **Skills (`/api/skills/`)**

| Método | Endpoint            | Descrição                      |
| ------ | ------------------- | ------------------------------ |
| GET    | `/api/skills/`      | Lista todas as skills          |
| POST   | `/api/skills/`      | Cria uma nova skill            |
| GET    | `/api/skills/{id}/` | Obtém os detalhes de uma skill |
| PUT    | `/api/skills/{id}/` | Atualiza uma skill existente   |
| DELETE | `/api/skills/{id}/` | Remove uma skill               |

---

## **Objetivo do Projeto**

Este projeto foi desenvolvido para **aprendizado e prática do Django REST Framework**, com foco na utilização do **ModelViewSet**, que facilita a criação de APIs RESTful ao fornecer uma implementação eficiente e estruturada das operações CRUD.

