Feature: Listar livros do usuário
  Como um usuário autenticado
  Eu quero listar os livros associados ao meu perfil
  Para verificar minha coleção

  Scenario: Listar livros do usuário com sucesso
    Given a URL base da API está configurada
    And o usuário está autenticado com um token
    When eu faço uma requisição GET para listar os livros do usuário
    Then o status code da resposta deve ser 200
    And os livros na resposta devem incluir os ISBNs adicionados
    And o ID e nome do usuário devem corresponder