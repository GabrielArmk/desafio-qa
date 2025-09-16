Feature: Preencher o formulário do demoqa

  Scenario: Preenchimento completo do formulário
    Given que eu acesso o site "https://demoqa.com"
    When eu preencho o formulário de Practice Form
    Then devo ver o modal de confirmação
