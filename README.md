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
  - [2. **user\_image**](#2-user_image)
    - [Endpoints](#endpoints-1)
    - [2.1. **Criação de uma imagem**](#21-criação-de-uma-imagem)
    - [`/users/image/`](#usersimage)
    - [Exemplo de Request:](#exemplo-de-request-6)
    - [Corpo da Requisição:](#corpo-da-requisição-6)
    - [Exemplo de Response:](#exemplo-de-response-6)
    - [Possíveis Erros:](#possíveis-erros-6)
    - [2.2 **listando todas as imagens**](#22-listando-todas-as-imagens)
    - [`/users/image`](#usersimage-1)
    - [Exemplo de Request:](#exemplo-de-request-7)
    - [Corpo da Requisição:](#corpo-da-requisição-7)
    - [Exemplo de Response:](#exemplo-de-response-7)
    - [Possíveis Erros:](#possíveis-erros-7)
    - [2.3 **listando imagem por id**](#23-listando-imagem-por-id)
    - [`/users/image/:id`](#usersimageid)
    - [Exemplo de Request:](#exemplo-de-request-8)
    - [Corpo da Requisição:](#corpo-da-requisição-8)
    - [Exemplo de Response:](#exemplo-de-response-8)
    - [Possíveis Erros:](#possíveis-erros-8)
    - [2.4 **editando imagem**](#24-editando-imagem)
    - [`/users/image/:id`](#usersimageid-1)
    - [Exemplo de Request:](#exemplo-de-request-9)
    - [Corpo da Requisição:](#corpo-da-requisição-9)
    - [Exemplo de Response:](#exemplo-de-response-9)
    - [Possíveis Erros:](#possíveis-erros-9)
    - [2.5 **Deletando Imagem**](#25-deletando-imagem)
    - [`/users/image/:id`](#usersimageid-2)
    - [Exemplo de Request:](#exemplo-de-request-10)
    - [Corpo da Requisição:](#corpo-da-requisição-10)
    - [Exemplo de Response:](#exemplo-de-response-10)
    - [Possíveis Erros:](#possíveis-erros-10)
  - [3. **Games**](#3-games)
    - [Endpoints](#endpoints-2)
    - [3.1 **Criação de um game**](#31-criação-de-um-game)
    - [`/games`](#games)
    - [Exemplo de Request:](#exemplo-de-request-11)
    - [Corpo da Requisição:](#corpo-da-requisição-11)
    - [Exemplo de Response:](#exemplo-de-response-11)
    - [Possíveis Erros:](#possíveis-erros-11)
    - [3.2 **listando Games**](#32-listando-games)
    - [`/games/`](#games-1)
    - [Exemplo de Request:](#exemplo-de-request-12)
    - [Corpo da Requisição:](#corpo-da-requisição-12)
    - [Exemplo de Response:](#exemplo-de-response-12)
    - [Possíveis Erros:](#possíveis-erros-12)
    - [3.3 **listando Games por id**](#33-listando-games-por-id)
    - [`/games/:id`](#gamesid)
    - [Exemplo de Request:](#exemplo-de-request-13)
    - [Exemplo de Response:](#exemplo-de-response-13)
    - [Possíveis Erros:](#possíveis-erros-13)
    - [3.4. **Atualização do game**](#34-atualização-do-game)
    - [`/games/:id`](#gamesid-1)
    - [Exemplo de Request:](#exemplo-de-request-14)
    - [Corpo da Requisição:](#corpo-da-requisição-13)
    - [Exemplo de Response:](#exemplo-de-response-14)
    - [Possíveis Erros:](#possíveis-erros-14)
    - [3.5. \**deleção do game*](#35-deleção-do-game)
    - [`/games/:id`](#gamesid-2)
    - [Exemplo de Request:](#exemplo-de-request-15)
    - [Corpo da Requisição:](#corpo-da-requisição-14)
    - [Exemplo de Response:](#exemplo-de-response-15)
    - [Possíveis Erros:](#possíveis-erros-15)
  - [4. **Reviews**](#4-reviews)
    - [Endpoints](#endpoints-3)
  - [4.1 **Criando uma review**](#41-criando-uma-review)
    - [`/reviews`](#reviews)
    - [Exemplo de Request:](#exemplo-de-request-16)
    - [Corpo da Requisição:](#corpo-da-requisição-15)
    - [Exemplo de Response:](#exemplo-de-response-16)
    - [Possíveis Erros:](#possíveis-erros-16)
    - [4.2. **Listar todos as reviews**](#42-listar-todos-as-reviews)
    - [`/reviews`](#reviews-1)
    - [Exemplo de Request:](#exemplo-de-request-17)
    - [Corpo da Requisição:](#corpo-da-requisição-16)
    - [Exemplo de Response:](#exemplo-de-response-17)
    - [Possíveis Erros:](#possíveis-erros-17)
    - [4.3 **listando Review por id**](#43-listando-review-por-id)
    - [`/reviews/:id`](#reviewsid)
    - [Exemplo de Request:](#exemplo-de-request-18)
    - [Exemplo de Response:](#exemplo-de-response-18)
    - [Possíveis Erros:](#possíveis-erros-18)
    - [4.4. **Atualização uma reviews**](#44-atualização-uma-reviews)
    - [`/reviews/:id`](#reviewsid-1)
    - [Exemplo de Request:](#exemplo-de-request-19)
    - [Corpo da Requisição:](#corpo-da-requisição-17)
    - [Exemplo de Response:](#exemplo-de-response-19)
    - [Possíveis Erros:](#possíveis-erros-19)
    - [4.5. \**deleção da review*](#45-deleção-da-review)
    - [`/reviews/:id`](#reviewsid-2)
    - [Exemplo de Request:](#exemplo-de-request-20)
    - [Corpo da Requisição:](#corpo-da-requisição-18)
    - [Exemplo de Response:](#exemplo-de-response-20)
    - [Possíveis Erros:](#possíveis-erros-20)
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

## 2. **user_image**

[ Voltar para os Endpoints ](#5-endpoints)

O objeto User é definido como:

| Campo       | Tipo    | Descrição                                  |
| ----------  | ------- | ------------------------------------------ |
| id          | string  | Identificador único da imagem              |
| user_image  | arquivo | arquivo de imagem                          |
| user        | objeto  | objeto User define o usuario dono da imagem|

### Endpoints

| Método | Rota               | Descrição                 |
| ------ | -------------------| ------------------------- |
| POST   | /users/image/      | Criação de imagem.        |
| GET    | /users/image/      | Lista todas as imagens    |
| GET    | /users/image/:id   | Lista uma imagem          |
| PATCH  | /users/image/:id   | Atualiza a imagem         |
| DELETE | /users/image/:id   | Deleta a imagem           |

---

### 2.1. **Criação de uma imagem**

[ Voltar para os Endpoints ](#5-endpoints)

### `/users/image/`

### Exemplo de Request:
```
POST /users/image
Host: https://mais-que-um-pet.herokuapp.com
Authorization: Bearer token
Content-type:multpart form
```multpart form


```
### Corpo da Requisição:

WebKitFormBoundary123456789
 user_image: arquivo de imagem
WebKitFormBoundary123456789

### Exemplo de Response:

```
201 Created

```

```json
[
{
	"id": 1,
	"user_image": "http://127.0.0.1:8000/media/media/WhatsApp_Image_2022-12-03_at_19.54.56.jpeg",
	"user": 2
}
]
```


### Possíveis Erros:

| Código do Erro  | Descrição                         |
| --------------- | --------------------------------- |
| 400 Bad request | missing authorization token.      |
| 403 forbidden   | Invalid token.                    |
| 400 Bad request | This image is already registered. |


---

### 2.2 **listando todas as imagens** 
 
[ Voltar para os Endpoints ](#5-endpoints)

### `/users/image`

### Exemplo de Request:

```
GET /users/image
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
200 Ok
```

```json
[
{
	"id": 1,
	"user_image": "http://127.0.0.1:8000/media/media/WhatsApp_Image_2022-12-03_at_19.54.56.jpeg",
	"user": 2
}
]
```
### Possíveis Erros:

Nenhum, o máximo que pode acontecer é retornar uma lista vazia.

---

### 2.3 **listando imagem por id**


[ Voltar para os Endpoints ](#5-endpoints)


### `/users/image/:id`


### Exemplo de Request:

```
GET /users/image
Host: https://mais-que-um-pet.herokuapp.com
Authorization:Bearer Token
Content-type: application/json
```

### Corpo da Requisição:

```json
Vazio
```

### Exemplo de Response:

```
200 Ok
```

```json
[
{
	"id": 1,
	"user_image": "http://127.0.0.1:8000/media/media/WhatsApp_Image_2022-12-03_at_19.54.56.jpeg",
	"user": 2
}
]
```
### Possíveis Erros:

| Código do Erro   | Descrição                     |
| ---------------- | ----------------------------- |
| 400 Bad request  | missing authorization token.  |
| 403 forbidden    | Invalid token.                |
| 404 not found    | image not found.              |

---

### 2.4 **editando imagem**

[ Voltar para os Endpoints ](#5-endpoints)


### `/users/image/:id`


### Exemplo de Request:
```
POST /users/image/:id
Host: https://mais-que-um-pet.herokuapp.com
Authorization: Bearer token
Content-type:multpart form
```

### Corpo da Requisição:

multpart form
```
WebKitFormBoundary123456789
 user_image: arquivo de imagem
WebKitFormBoundary123456789
```
### Exemplo de Response:

```
200 Ok
```

```json
[
{
	"id": 1,
	"user_image": "http://127.0.0.1:8000/media/media/WhatsApp_Image_2022-12-03_at_19.54.56.jpeg",
	"user": 2
}
]
```
### Possíveis Erros:

| Código do Erro   | Descrição                     |
| ---------------- | ----------------------------- |
| 400 Bad request  | missing authorization token.  |
| 403 forbidden    | Invalid token.                |
| 404 not found    | image not found.              |

---

### 2.5 **Deletando Imagem** 


[ Voltar para os Endpoints ](#5-endpoints)


### `/users/image/:id`


### Exemplo de Request:
```
POST /users/image/:id
Host: https://mais-que-um-pet.herokuapp.com
Authorization: Bearer token

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
| 404 not found    | image not found.                               |
| 401 unauthorized | Only superusers can delete anothers image.     |

---


## 3. **Games**

[ Voltar para os Endpoints ](#5-endpoints)

O objeto Game é definido como:

| Campo             | Tipo    | Descrição                                            |
| ----------------- | ------- | ---------------------------------------------------- |
| id                | string  | Identificador único do game                          |
| game_name         | string  | O nome do game                                       |
| description       | string  | descrição do game                                    |
| game_logo         | string  | url da imagem do game                                |
| made_by           | string  | empresa ou criador do game                           |
| users_avaliations | integer | é a media de todas avaliações de usuarios            |
| number_of_reviews | integer | numero de usuarios que fizeram reviews desse game    |
| genders           | array   | array de um ou mais objetos definindo genero do game |

### Endpoints

| Método | Rota               | Descrição                                 |
| ------ | -------------------| ------------------------------------------|
| POST   | /games/            | Criação de game                           |
| GET    | /games/            | Lista todas lista todos os games          |
| GET    | /games/:id         | Lista um game                             |
| PATCH  | /games/:id         | Atualiza o game                           |
| DELETE | /games/:id         | Deleta o game                             |

---

### 3.1 **Criação de um game**

### `/games`

### Exemplo de Request:

```
POST /games
Host: https://dubairrobackend.onrender.com/
Authorization: bearer token
Content-type: application/json

```

### Corpo da Requisição:

```json

[
  {
    "id": 1,
    "name_game": "The Legend of Zelda: Breath of the Wild",
    "description": "The Legend of Zelda: Breath of the Wild is an action-adventure game...",
    "game_logo": "http://example.com/media/zelda.jpg",
    "made_by": "Nintendo",
    "genders": [
      {
        "name": "Adventure",
      },
      {
        "name": "Action",
      }
    ]
  }
  
]
  


```

OBS.: Chaves não presentes no schema serão removidas. 
      Se o is_superuser não for fornecido sera automaticamnte prenchido como false. 

### Exemplo de Response:

```
201 Created

```

```json
[
	{
  "id": 1,
  "name_game": "The Legend of Zelda: Breath of the Wild",
  "description": "The Legend of Zelda: Breath of the Wild is an action-adventure game...",
  "game_logo": "http://example.com/media/zelda.jpg",
  "made_by": "Nintendo",
  "users_avaliations": 8.5,
  "number_of_reviews": 10,
  "genders": [
    {
      "id": 1,
      "name": "Adventure",
      "created_at": "2022-01-01"
    },
    {
      "id": 2,
      "name": "Action",
      "created_at": "2022-01-01"
    }
  ]
}
]
```

### Possíveis Erros:

| Código do Erro   | Descrição                                          |
| ---------------  | ---------------------------------------------------|
| 400 Bad request  |  Game with this name_game already exists.          |
| 400 Bad request  |  name_game This field may not be blank.            |
| 400 Bad request  |  genders this list may not be empty.               |
| 400 Bad request  |  Missing authorization token.                      |
| 403 forbidden    |  Invalid token.                                    |
| 401 unauthorized |  Only superusers can delete games.                 |

--- 

### 3.2 **listando Games**

 
[ Voltar para os Endpoints ](#5-endpoints)

### `/games/`

### Exemplo de Request:

```
GET /games
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
200 Ok
```

```json
[
	{
  "id": 1,
  "name_game": "The Legend of Zelda: Breath of the Wild",
  "description": "The Legend of Zelda: Breath of the Wild is an action-adventure game...",
  "game_logo": "http://example.com/media/zelda.jpg",
  "made_by": "Nintendo",
  "users_avaliations": 8.5,
  "number_of_reviews": 10,
  "genders": [
    {
      "id": 1,
      "name": "Adventure",
      "created_at": "2022-01-01"
    },
    {
      "id": 2,
      "name": "Action",
      "created_at": "2022-01-01"
    }
  ]
}
]
```
### Possíveis Erros:

Nenhum, o máximo que pode acontecer é retornar uma lista vazia.

---

### 3.3 **listando Games por id**

[ Voltar aos Endpoints ](#5-endpoints)

### `/games/:id`

### Exemplo de Request:

GET /user
Host: https://mais-que-um-pet.herokuapp.com
Authorization: Bearer token
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
  "name_game": "The Legend of Zelda: Breath of the Wild",
  "description": "The Legend of Zelda: Breath of the Wild is an action-adventure game...",
  "game_logo": "http://example.com/media/zelda.jpg",
  "made_by": "Nintendo",
  "users_avaliations": 8.5,
  "number_of_reviews": 10,
  "genders": [
    {
      "id": 1,
      "name": "Adventure",
      "created_at": "2022-01-01"
    },
    {
      "id": 2,
      "name": "Action",
      "created_at": "2022-01-01"
    }
  ]
}
]
```

### Possíveis Erros:

| Código do Erro | Descrição       |
| -------------- | --------------- |
| 404 Not Found  | game not found. |

---

### 3.4. **Atualização do game**

[ Voltar aos Endpoints ](#5-endpoints)

### `/games/:id`

```
Pode ser atualizado todos os campos com exeção de id,users_avaliation e number_of_reviews.
```

### Exemplo de Request:

```

PATCH /gamer/:id
Host: https://mais-que-um-pet.herokuapp.com
Authorization: Bearer token
Content-type: application/json

```

### Corpo da Requisição:

```json
{
  "game_name": "Zeldinha",
  
}
```

### Exemplo de Response:

```
200 OK
```

```json
[
	{
  "id": 1,
  "name_game": "Zeldinha",
  "description": "The Legend of Zelda: Breath of the Wild is an action-adventure game...",
  "game_logo": "http://example.com/media/zelda.jpg",
  "made_by": "Nintendo",
  "users_avaliations": 8.5,
  "number_of_reviews": 10,
  "genders": [
    {
      "id": 1,
      "name": "Adventure",
      "created_at": "2022-01-01"
    },
    {
      "id": 2,
      "name": "Action",
      "created_at": "2022-01-01"
    }
  ]
}
]
```

### Possíveis Erros:

| Código do Erro   | Descrição                                      |
| ---------------- | -------------------------------------          |
| 400 Bad request  | missing authorization token.                   |
| 403 forbidden    | Invalid token.                                 |
| 401 unauthorized | Is not able to update users_avaliations value. |
| 401 unauthorized | Is not able to update number_of_reviews value. |
| 401 unauthorized | Is not able to update id.                      |
| 404 not found    | game not found.                                |

---

### 3.5. **deleção do game*

[ Voltar aos Endpoints ](#5-endpoints)

### `/games/:id`

### Exemplo de Request:

```

DELETE /users/:id
Host: https://mais-que-um-pet.herokuapp.com
Authorization: Bearer token
Content-type: application/json

```

### Corpo da Requisição:

```json
Vazio
```

### Exemplo de Response:

```
204 OK
```

```json
Vazio
```

### Possíveis Erros:

| Código do Erro   | Descrição                     |
| ---------------- | ----------------------------- |
| 400 Bad request  | missing authorization token.. |
| 403 forbidden    | Invalid token.                |
| 404 not found    | game not found.               |


---

## 4. **Reviews**

[ Voltar para os Endpoints ](#5-endpoints)

O objeto User é definido como:

| Campo         | Tipo     | Descrição                               |
| ------------- | -------- | --------------------------------------- |
| id            | number   | Identificador único de review           |
| review        | string   | avaliação do game feito pelo usuario.   |
| created_at    | date     | Data de cadastro de criação da review   |
| user          | number   | id do usuario que fez a review.         |
| game          | number   | id do game que esta recebendo a review  |
| rate          | number   | nota de 0 a 10 definida pelo usuario    |
| user_email    | string   | email do usuario que fez a review       |


### Endpoints

| Método | Rota           | Descrição                             |
| ------ | -------------- | ------------------------------------- |
| POST   | /pet           | Criação de uma review                 |
| GET    | /pet           | Lista todos as reviews                |
| GET    | /pet/:id       | Lista a review pelo id                |
| PATCH  | /pet/:id       | Atualiza dados da review              |
| DELETE | /pet/:id       | deleção da review                     |

---

## 4.1 **Criando uma review**

[ Voltar para os Endpoints ](#5-endpoints)

### `/reviews`

### Exemplo de Request:

```
POST /reviews
Host: https://mais-que-um-pet.herokuapp.com
Authorization: Bearer token
Content-type: application/json
```

### Corpo da Requisição:

```json
{
	"review":"jogo brabo dms slk tem como não",
	"game" : 51,
	"rate":7
}
```

### Exemplo de Response:

```
201 Created
```

```json
{
		"id": 38,
		"review": "top",
		"user": 4,
		"game": 51,
		"rate": 7,
		"email_usuario": "havyel@email.com"
	}
```

### Possíveis Erros:
```

| Código do Erro  | Descrição                                       |
| --------------- | ------------------------------------------------|
| 403 forbidden   | Invalid token.                                  |
| 400 Bad request | missing authorization token.                    |
| 400 Bad request | game: Invalid pk - object does not exist.|
| 400 Bad request | "\"11\" is not a valid choice.                  |

Obs: o field rate aceita penas inteiros de 0 a 10, qualquer valor diferente disso retornara um erro com valor colocado junto a um :  is not a valid choice.
```
---

### 4.2. **Listar todos as reviews**

[ Voltar para os Endpoints ](#5-endpoints)

### `/reviews`

### Exemplo de Request:

```
GET /pet
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
200 Ok
```

```json
[
	{
		"id": 1,
		"review": "jogo brabo dms slk tem como não",
		"user": 2,
		"game": 1,
		"rate": 7,
		"review_made_by": "exemplo2"
	}
]
```

### Possíveis Erros:

Nenhum, o máximo que pode acontecer é retornar uma lista vazia.

---


### 4.3 **listando Review por id**

[ Voltar aos Endpoints ](#5-endpoints)

### `/reviews/:id`

### Exemplo de Request:

GET /reviews/:id
Host: https://mais-que-um-pet.herokuapp.com
Authorization: Bearer token
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
		"review": "jogo brabo dms slk tem como não",
		"user": 2,
		"game": 1,
		"rate": 7,
		"review_made_by": "exemplo2"
	}
]
```

### Possíveis Erros:

| Código do Erro   | Descrição                     |
| ---------------- | ----------------------------- |
| 400 Bad request  | missing authorization token.. |
| 403 forbidden    | Invalid token.                |
| 404 not found    | review not found.             |
```
---
```
### 4.4. **Atualização uma reviews**

[ Voltar aos Endpoints ](#5-endpoints)

### `/reviews/:id`

```
É permitido atualizar apenas o campo review e o campo rate.
```

### Exemplo de Request:

```

PATCH /gamer/:id
Host: https://mais-que-um-pet.herokuapp.com
Authorization: Bearer token
Content-type: application/json

```

### Corpo da Requisição:

```json
{
  "review": "mudei de ideia na verdade o jogo e mais ou menos ",
  "rate":5
  
}
```

### Exemplo de Response:

```
200 OK
```

```json
[
	

{
		"id": 38,
		"review": "mudei de ideia na verdade o jogo e mais ou menos",
		"user": 4,
		"game": 51,
		"rate": 5,
		"review_made_by": "exemplo2"
	}


]
```

### Possíveis Erros:

| Código do Erro   | Descrição                                      |
| ---------------- | -------------------------------------          |
| 400 Bad request  | missing authorization token.                   |
| 403 forbidden    | Invalid token.                                 |
| 401 unauthorized | Is not able to update id value.                |
| 401 unauthorized | Is not able to update review_made_by  value.   |
| 401 unauthorized | Is not able to update game value.              | 
| 401 unauthorized | Is not able to update user value.              |
| 404 not found    | review not found.                              |

---

### 4.5. **deleção da review*

[ Voltar aos Endpoints ](#5-endpoints)

### `/reviews/:id`

### Exemplo de Request:

```

DELETE /reviews/:id
Host: https://mais-que-um-pet.herokuapp.com
Authorization: Bearer token
Content-type: application/json

```

### Corpo da Requisição:

```json
Vazio
```

### Exemplo de Response:

```
204 OK
```

```json
Vazio
```

### Possíveis Erros:

| Código do Erro   | Descrição                     |
| ---------------- | ----------------------------- |
| 400 Bad request  | missing authorization token.. |
| 403 forbidden    | Invalid token.                |
| 404 not found    | review not found.             |


---