Feature: Listar livros disponíveis
  Como um usuário do sistema
  Eu quero listar os livros disponíveis
  Para obter os ISBNs dos livros

  Scenario: Listar livros com sucesso
    Given a URL base da API está configurada
    When eu faço uma requisição GET para listar livros
    Then o status code da resposta deve ser 200
    And os ISBNs dos livros 1 e 3 devem ser salvos