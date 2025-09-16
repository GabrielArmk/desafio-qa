import pytest
import requests
import random
import uuid

class dados():
    url_base = "https://demoqa.com"
    sufixo_unico = uuid.uuid4().hex[:8]
    nome_usuario = f"teste_{sufixo_unico}"
    senha = "Teste12345!" 
    id_user = None
    id_token = None
    livro1 = None
    livro3 = None
    
def test_usuario_id():
    url_user = dados.url_base + "/Account/v1/User"
    corpo = {"userName": dados.nome_usuario, "password": dados.senha}
    resposta = requests.post(url_user, json=corpo)
    
    # valida o status code
    assert resposta.status_code == 201, f"Falha ao criar usuário: {resposta.text}"
    
    id_user = resposta.json()["userID"]   
    dados.id_user = id_user

def test_token_acesso():
    url_token = dados.url_base + "/Account/v1/GenerateToken"
    corpo_token = {"userName": dados.nome_usuario, "password": dados.senha}
    resposta_token = requests.post(url_token, json=corpo_token)
    
    # saval variavel token na classe dados
    id_token = resposta_token.json()["token"]
    dados.id_token = id_token

    # valida o status code
    assert resposta_token.status_code == 200, f"Falha ao gerar token: {resposta_token.text}"

def test_autorizacao():
    url_token = dados.url_base + "/Account/v1/authorized"
    corpo_token = {"userName": dados.nome_usuario, "password": dados.senha}
    resposta_token = requests.post(url_token, json=corpo_token)
    
    # valida o status code
    assert resposta_token.status_code == 200
    assert resposta_token.json() is True, f"Falha na autorização: {resposta_token.text}"
    
def test_listar_livros():
    url_livros = dados.url_base + "/BookStore/v1/Books"
    resposta_livros = requests.get(url_livros)
    
    # valida o status code
    assert resposta_livros.status_code == 200, f"Falha ao listar livros: {resposta_livros.text}"
    
    dados.livro1 = resposta_livros.json()["books"][0]["isbn"]
    dados.livro3 = resposta_livros.json()["books"][2]["isbn"]

def test_adicionar_livros():
    url_add_livros = dados.url_base + "/BookStore/v1/Books"
    body= {
        "userId": dados.id_user,
        "collectionOfIsbns": [
            {
                "isbn": dados.livro1
            },
            {
                "isbn": dados.livro3
            }
        ]
    }
    headers = {
        "Authorization" : f"Bearer {dados.id_token}"
    }
    resposta_add = requests.post(url_add_livros, headers=headers, json=body)

    # aqui faz algumas validações
    assert resposta_add.status_code == 201, f"Falha ao adicionar livro: {resposta_add.text}"
    assert resposta_add.json()["books"][0]["isbn"] == dados.livro1
    assert resposta_add.json()["books"][1]["isbn"] == dados.livro3

def test_listar_livros_usuario():
    url_user = dados.url_base + f"/Account/v1/User/{dados.id_user}"
    headers = {
        "Authorization" : f"Bearer {dados.id_token}"
    }
    resposta_user = requests.get(url_user, headers=headers)
    
    # aqui faz algumas validações
    assert resposta_user.status_code == 200, f"Falha ao listar livros do usuário: {resposta_user.text}"
    assert resposta_user.json()["userId"] == dados.id_user
    assert resposta_user.json()["username"] == dados.nome_usuario

    # valida se os livros estão na lista do usuário
    books = resposta_user.json()["books"]
    isbns_usuario = [livro["isbn"] for livro in books]
    assert dados.livro1 in isbns_usuario, "Livro 1 não encontrado na lista do usuário"
    assert dados.livro3 in isbns_usuario, "Livro 3 não encontrado na lista do usuário"