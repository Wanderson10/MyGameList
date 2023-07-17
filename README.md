# Documentação da API

## Tabela de Conteúdos
- [Documentação da API](#documentação-da-api)
  - [Tabela de Conteúdos](#tabela-de-conteúdos)
  - [1. Visão Geral](#1-visão-geral)
  - [2. Início Rápido](#2-início-rápido)
    - [2.1. Instalando Dependências](#21-instalando-dependências)
    - [2.2 Variáveis de Ambiente](#22-variáveis-de-ambiente)
    - [2.3. Migrations](#23-migrations)
  - [1. \**users*](#1-users)
    - [Endpoints](#endpoints)
    - [1.1. **Criação de usuarios**](#11-criação-de-usuarios)
    - [`/users`](#users)
    - [Exemplo de Request:](#exemplo-de-request)
    - [Corpo da Requisição:](#corpo-da-requisição)
    - [Exemplo de Response:](#exemplo-de-response)
    - [Possíveis Erros:](#possíveis-erros)
    - [1.2. **Login do usuário**](#12-login-do-usuário)
    - [Exemplo de Request:](#exemplo-de-request-1)
    - [Corpo da Requisição:](#corpo-da-requisição-1)
    - [Exemplo de Response:](#exemplo-de-response-1)
    - [Possíveis Erros:](#possíveis-erros-1)
    - [1.3. **Listando Usuários**](#13-listando-usuários)
    - [`/users`](#users-1)
    - [Exemplo de Request:](#exemplo-de-request-2)
    - [Corpo da Requisição:](#corpo-da-requisição-2)
    - [Exemplo de Response:](#exemplo-de-response-2)
    - [Possíveis Erros:](#possíveis-erros-2)
    - [1.4. **Listando Usuário**](#14-listando-usuário)
    - [`/user/:id`](#userid)
    - [Exemplo de Request:](#exemplo-de-request-3)
    - [Corpo da Requisição:](#corpo-da-requisição-3)
    - [Exemplo de Response:](#exemplo-de-response-3)
    - [Possíveis Erros:](#possíveis-erros-3)
    - [1.5. **Atualização do usuário**](#15-atualização-do-usuário)
    - [`/company/:id`](#companyid)
    - [Exemplo de Request:](#exemplo-de-request-4)
    - [Corpo da Requisição:](#corpo-da-requisição-4)
    - [Exemplo de Response:](#exemplo-de-response-4)
    - [Possíveis Erros:](#possíveis-erros-4)
    - [1.6. **Deletar o usuário**](#16-deletar-o-usuário)
    - [`/user/:id`](#userid-1)
    - [Exemplo de Request:](#exemplo-de-request-5)
    - [Corpo da Requisição:](#corpo-da-requisição-5)
    - [Exemplo de Response:](#exemplo-de-response-5)
    - [Possíveis Erros:](#possíveis-erros-5)
---
## 1. Visão Geral

Visão geral do projeto, um pouco das tecnologias usadas.

- [Python](https://docs.python.org/3/)
- [Django](https://docs.djangoproject.com/en/4.2/)
- [Django_REST_framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

A URL base da aplicação:

https://dubairrobackend.onrender.com/

---
## 2. Início Rápido

[ Voltar para o topo ](#tabela-de-conteúdos)

### 2.1. Instalando Dependências

Clone o projeto em sua máquina e instale as dependências com o comando:

```pip freeze > requirements.txt
```


### 2.2 Variáveis de Ambiente

Em seguida, crie um arquivo **.env**, copiando o formato do arquivo **.env.example**:

```
cp .env.example .env
```

Configure suas variáveis de ambiente com suas credenciais do Postgres e uma nova database da sua escolha.

### 2.3. Migrations

Execute as migrations com o comando:

```
python manage.py migrate
```

---
## 1. **users*

[ Voltar para os Endpoints ](#5-endpoints)

O objeto User é definido como:

| Campo       | Tipo    | Descrição                                  |
| ----------  | ------- | ------------------------------------------ |
| id          | string  | Identificador único da empresa             |
| username    | string  | O nome do usuario                          |
| email       | string  | O e-mail do usuário.                       |
| password    | string  | A senha de acesso do usuário               |
| date_joined | date    | Data de cadastro do usuario                |
| phone_number| string  | Objeto Contact, define contatos do usuário |
| is_superuser| boolean |  define se o usuario é admistrador         |

### Endpoints

| Método | Rota          | Descrição                 |
| ------ | ----------    | ------------------------- |
| POST   | /users        | Criação de um usuário.    |
| POST   | /users/login/ | Login do usuário.         |
| GET    | /users        | Lista todos os usuários   |
| GET    | /users/:id    | Lista um usuário          |
| PATCH  | /users/:id    | Atualiza dados do usuário |
| DELETE | /users/:id    | Deleta o usuário          |

---

### 1.1. **Criação de usuarios**

[ Voltar para os Endpoints ](#5-endpoints)

### `/users`

### Exemplo de Request:

```
POST /users
Host: https://dubairrobackend.onrender.com/
Authorization: None
Content-type: application/json

```

### Corpo da Requisição:

```json

{
  "username": "exemplo2",
  "email": "exemplo2@example.com",
  "phone_number": "123456789",
  "password": "senha123",
  "is_superuser" : true,
}
  


```

OBS.: Chaves não presentes no schema serão removidas. 
      Se o is_superuser não for fornecido sera automaticamnte prenchido como false. 

### Exemplo de Response:

```
201 Created

```

```json

	{
	"id": 2,
	"username": "exemplo2",
	"email": "exemplo2@example.com",
	"date_joined": "2023-07-14",
	"phone_number": "123456789",
	"is_superuser": true
}

```

### Possíveis Erros:

| Código do Erro  | Descrição                                 |
| --------------- | ---------------------                     |
| 400 Bad request | user with this email already exists.      |
| 400 Bad request | A user with that username already exists. |

--- 

### 1.2. **Login do usuário**

[ Voltar aos Endpoints ](#5-endpoints)

### Exemplo de Request:

```
POST /users/login/
Host: https://mais-que-um-pet.herokuapp.com
Authorization: None
Content-type: application/json
```

### Corpo da Requisição:

```json
{
  "username": "userteste",
  "password": "1234"
}
```

### Exemplo de Response:

```
200 OK
```

```json
[
  
	{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4OTQ1Mzk1MSwiaWF0IjoxNjg5MzY3NTUxLCJqdGkiOiJjNzJlYmVlYWRlNWQ0OTY4YjU2MzU1ZDExNWVjMmEwMCIsInVzZXJfaWQiOjJ9.vKHnnf_dG8eSGhCBi3b9xVptVC6-I1IHnKF8o4LCsu4",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MzY4OTkxLCJpYXQiOjE2ODkzNjc1NTEsImp0aSI6ImEwM2FmNWZkOWI2ZjQ0MTE4OGMwZWUwOTZlYjlmOThlIiwidXNlcl9pZCI6Mn0.5VqzzYTBcCj4Pqjh4fJd13wn9yCVycGiZK9KGpaTwIg",
	"user": {
		"id": 2,
		"userteste": "exemplo2",
		"email": "exemplo2@example.com",
		"date_joined": "2023-07-14",
		"phone_number": "123456789",
		"is_superuser": false
	}

	
}
]
```

### Possíveis Erros:

| Código do Erro  | Descrição                   |
| --------------- | --------------------------- |
| 400 Bad request | email/password is required. |
| 403 forbidden   | Wrong email/password.       |

---

### 1.3. **Listando Usuários**

[ Voltar aos Endpoints ](#5-endpoints)

### `/users`

### Exemplo de Request:

```

GET /users
Host: https://mais-que-um-pet.herokuapp.com
Authorization: None
Content-type: application/json

```

### Corpo da Requisição:

```json
Vazio
```

### Exemplo de Response:

```
200 OK
```

```json
[
	{
		"id": 1,
		"username": "exemplo",
		"email": "exemplo@example.com",
		"date_joined": "2023-07-14",
		"phone_number": "123456789",
		"is_superuser": false
	},
	{
		"id": 2,
		"username": "exemplo2",
		"email": "exemplo2@example.com",
		"date_joined": "2023-07-14",
		"phone_number": "123456789",
		"is_superuser": false
	}
]
```

### Possíveis Erros:

Nenhum, o máximo que pode acontecer é retornar uma lista vazia.

---
### 1.4. **Listando Usuário**

[ Voltar aos Endpoints ](#5-endpoints)

### `/user/:id`

### Exemplo de Request:

```

GET /user
Host: https://mais-que-um-pet.herokuapp.com
Authorization: Bearer token
Content-type: application/json

```

### Corpo da Requisição:

```   json Vazio
```

### Exemplo de Response:

```
200 OK
```

```json
	{
	{
		"id": 2,
		"username": "exemplo2",
		"email": "exemplo2@example.com",
		"date_joined": "2023-07-14",
		"phone_number": "123456789",
		"is_superuser": false
	}
	},

```

### Possíveis Erros:

| Código do Erro | Descrição       |
| -------------- | --------------- |
| 404 Not Found  | User not found. |

---

### 1.5. **Atualização do usuário**

[ Voltar aos Endpoints ](#5-endpoints)

### `/company/:id`

```
Pode ser atualizado o user_name, user_image, email e password.
```

### Exemplo de Request:

```

PATCH /users/:id
Host: https://mais-que-um-pet.herokuapp.com
Authorization: Bearer token
Content-type: application/json

```

### Corpo da Requisição:

```json
{
 {"username":"user"}
}
```

### Exemplo de Response:

```
200 OK
```

```json
{
	{
	"id": 1,
	"username": "user",
	"email": "exemplo@example.com",
	"date_joined": "2023-07-14",
	"phone_number": "123456789",
	"is_superuser": false
    }
}
```

### Possíveis Erros:

| Código do Erro   | Descrição                             |
| ---------------- | ------------------------------------- |
| 400 Bad request  | missing authorization token..         |
| 403 forbidden    | Invalid token.                        |
| 401 unauthorized | Is not able to update id.             |
| 401 unauthorized | Is not able to update is_superuser    |
| 404 not found    | User not found.                       |

---

### 1.6. **Deletar o usuário**

[ Voltar aos Endpoints ](#5-endpoints)

### `/user/:id`

### Exemplo de Request:

```

DELETE /users/:id
Host: https://mais-que-um-pet.herokuapp.com
Authorization: Bearer token
Content-type: application/json

```

### Corpo da Requisição:

```   json Vazio
```

### Exemplo de Response:

```
204 OK
```

```  
 json Vazio
```

### Possíveis Erros:

| Código do Erro   | Descrição                                      |
| ---------------- | -----------------------------------------------|
| 400 Bad request  | Missing authorization token.                   |
| 403 forbidden    | Invalid token.                                 |
| 404 not found    | User not found.                                |
| 401 unauthorized | Only superusers can delete anothers users.     |


---

