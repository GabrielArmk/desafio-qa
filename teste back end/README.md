# Projeto de Testes de API com Behave

Este projeto contém testes automatizados para uma API REST (DemoQA) utilizando o framework **Behave** em Python, seguindo a abordagem de **Behavior-Driven Development (BDD)**. Os testes validam funcionalidades como criação de usuário, geração de token, autorização, listagem de livros, adição de livros à coleção de um usuário e verificação da coleção do usuário.

## Estrutura do Projeto

A estrutura de pastas e arquivos segue as convenções do Behave, garantindo organização e modularidade. Cada teste é representado por uma feature separada, com cenários descritos em Gherkin e implementações em Python.


### Descrição dos Arquivos e Pastas

- **`/features/`**: Contém todos os arquivos relacionados aos testes do Behave.
  - **`01_user_id.feature`**: Define o cenário para criar um usuário e obter seu ID.
  - **`02_token_acesso.feature`**: Define o cenário para gerar um token de acesso para autenticação.
  - **`03_autorizacao.feature`**: Define o cenário para verificar se um usuário está autorizado.
  - **`04_listar_livros.feature`**: Define o cenário para listar livros disponíveis na API.
  - **`05_adicionar_livros.feature`**: Define o cenário para adicionar livros à coleção de um usuário autenticado.
  - **`06_listar_livros_usuario.feature`**: Define o cenário para listar os livros associados ao perfil de um usuário.
  - **`/steps/`**: Subpasta contendo os arquivos Python que implementam a lógica dos passos.
    - **`steps.py`**: Contém as implementações dos passos definidos nos arquivos `.feature`, utilizando a biblioteca `requests` para chamadas HTTP.
    - **`dados.py`**: Define a classe `dados`, que armazena variáveis compartilhadas entre os testes, como `url_base`, `nome_usuario`, `id_user`, `id_token`, `livro1` e `livro3`.
  - **`environment.py`**: Configura o ambiente de teste, reinicializando os atributos mutáveis da classe `dados` antes de todas as features para garantir um estado limpo.

- **`requirements.txt`**: Lista as dependências do projeto (ex.: `behave`, `requests`).

- **`README.md`**: Este arquivo, que documenta o projeto, sua estrutura e instruções de uso.

## Pré-requisitos

- **Python**: Versão 3.8 ou superior.
- **pip**: Gerenciador de pacotes do Python.
- **Ambiente virtual** (opcional, mas recomendado): Para isolar as dependências.

## Instalação

1. Clone o repositório ou copie os arquivos para um diretório local.
2. Crie e ative um ambiente virtual (opcional):
   ```bash
   python -m venv venv
   venv\Scripts\activate     # Windows
3. Instale as dependências listadas em requirements.txt
    pip install -r requirements.txt
4. Como Executar os Testes:
    Certifique-se de estar no diretório raiz do projeto (onde está o arquivo requirements.txt).
    Execute os testes com o comando:
        behave
    O Behave executará todas as features na ordem definida pelos nomes dos arquivos (prefixados com números para garantir a sequência correta: criação de usuário, geração de token, etc.).
    A saída no terminal mostrará o resultado de cada cenário (passou, falhou ou erro).