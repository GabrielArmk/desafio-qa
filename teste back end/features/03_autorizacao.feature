Feature: Verificar autorização do usuário
  Como um usuário do sistema
  Eu quero verificar minha autorização
  Para garantir que minhas credenciais são válidas

  Scenario: Verificar autorização com sucesso
    Given a URL base da API está configurada
    When eu faço uma requisição POST para verificar autorização com nome e senha
    Then o status code da resposta deve ser 200
    And a resposta deve confirmar que o usuário está autorizado