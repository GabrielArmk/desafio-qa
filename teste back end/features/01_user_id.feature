Feature: Criar usuário e obter ID
  Como um usuário do sistema
  Eu quero criar um usuário
  Para obter um ID de usuário válido

  Scenario: Criar um novo usuário com sucesso
    Given a URL base da API está configurada
    When eu faço uma requisição POST para criar um usuário com nome e senha
    Then o status code da resposta deve ser 201
    And o ID do usuário deve ser salvo