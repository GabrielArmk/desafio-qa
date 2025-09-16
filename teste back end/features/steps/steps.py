from behave import given, when, then
import requests
from dados import dados

@given('a URL base da API está configurada')
def step_url_base_configurada(context):
    context.url_base = dados.url_base
    context.nome_usuario = dados.nome_usuario
    context.senha = dados.senha

@when('eu faço uma requisição POST para criar um usuário com nome e senha')
def step_criar_usuario(context):
    url_user = context.url_base + "/Account/v1/User"
    corpo = {"userName": context.nome_usuario, "password": context.senha}
    context.response = requests.post(url_user, json=corpo)

@then('o status code da resposta deve ser {status:d}')
def step_verificar_status(context, status):
    assert context.response.status_code == status, f"Falha na requisição: {context.response.text}"

@then('o ID do usuário deve ser salvo')
def step_salvar_id_usuario(context):
    dados.id_user = context.response.json()["userID"]

@when('eu faço uma requisição POST para gerar um token com nome e senha')
def step_gerar_token(context):
    url_token = context.url_base + "/Account/v1/GenerateToken"
    corpo_token = {"userName": context.nome_usuario, "password": context.senha}
    context.response = requests.post(url_token, json=corpo_token)

@then('o token deve ser salvo')
def step_salvar_token(context):
    dados.id_token = context.response.json()["token"]

@when('eu faço uma requisição POST para verificar autorização com nome e senha')
def step_verificar_autorizacao(context):
    url_token = context.url_base + "/Account/v1/authorized"
    corpo_token = {"userName": context.nome_usuario, "password": context.senha}
    context.response = requests.post(url_token, json=corpo_token)

@then('a resposta deve confirmar que o usuário está autorizado')
def step_confirmar_autorizacao(context):
    assert context.response.json() is True, f"Falha na requisição: {context.response.text}"

@when('eu faço uma requisição GET para listar livros')
def step_listar_livros(context):
    url_livros = context.url_base + "/BookStore/v1/Books"
    context.response = requests.get(url_livros)

@then('os ISBNs dos livros 1 e 3 devem ser salvos')
def step_salvar_isbns(context):
    dados.livro1 = context.response.json()["books"][0]["isbn"]
    dados.livro3 = context.response.json()["books"][2]["isbn"]

@given('o usuário está autenticado com um token')
def step_usuario_autenticado(context):
    context.headers = {"Authorization": f"Bearer {dados.id_token}"}

@when('eu faço uma requisição POST para adicionar livros com ISBNs')
def step_adicionar_livros(context):
    url_add_livros = context.url_base + "/BookStore/v1/Books"
    body = {
        "userId": dados.id_user,
        "collectionOfIsbns": [
            {"isbn": dados.livro1},
            {"isbn": dados.livro3}
        ]
    }
    context.response = requests.post(url_add_livros, headers=context.headers, json=body)

@then('os livros adicionados devem corresponder aos ISBNs enviados')
def step_verificar_livros_adicionados(context):
    assert context.response.json()["books"][0]["isbn"] == dados.livro1
    assert context.response.json()["books"][1]["isbn"] == dados.livro3

@when('eu faço uma requisição GET para listar os livros do usuário')
def step_listar_livros_usuario(context):
    url_user = context.url_base + f"/Account/v1/User/{dados.id_user}"
    context.response = requests.get(url_user, headers=context.headers)

@then('os livros na resposta devem incluir os ISBNs adicionados')
def step_verificar_livros_usuario(context):
    books = context.response.json()["books"]
    isbns_usuario = [livro["isbn"] for livro in books]
    assert dados.livro1 in isbns_usuario, "Livro 1 não encontrado na lista do usuário"
    assert dados.livro3 in isbns_usuario, "Livro 3 não encontrado na lista do usuário"

@then('o ID e nome do usuário devem corresponder')
def step_verificar_usuario(context):
    assert context.response.json()["userId"] == dados.id_user
    assert context.response.json()["username"] == context.nome_usuario