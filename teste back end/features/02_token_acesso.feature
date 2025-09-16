Feature: Gerar token de acesso
  Como um usuário do sistema
  Eu quero gerar um token de acesso
  Para autenticar minhas requisições

  Scenario: Gerar token de acesso com sucesso
    Given a URL base da API está configurada
    When eu faço uma requisição POST para gerar um token com nome e senha
    Then o status code da resposta deve ser 200
    And o token deve ser salvo