Feature: Abrir nova janela no demoqa

  Scenario: Validar abertura de nova janela
    Given que eu acesso o site "https://demoqa.com"
    When navego no meu e clico em new windows
    Then devo ver nova janela com uma mensagem e fechar
