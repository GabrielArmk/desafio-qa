Feature: Adicionar livros à coleção do usuário
  Como um usuário autenticado
  Eu quero adicionar livros à minha coleção
  Para associar livros ao meu perfil

  Scenario: Adicionar livros com sucesso
    Given a URL base da API está configurada
    And o usuário está autenticado com um token
    When eu faço uma requisição POST para adicionar livros com ISBNs
    Then o status code da resposta deve ser 201
    And os livros adicionados devem corresponder aos ISBNs enviados