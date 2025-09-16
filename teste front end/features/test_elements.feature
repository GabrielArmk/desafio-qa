Feature: Manipular registros web tables

  Scenario: Criar, editar e deletar um registro em web tables
    Given que eu acesso o site "https://demoqa.com"
    When crio um elemento
    When edito um elemento
    Then devo deletar o elemento criado