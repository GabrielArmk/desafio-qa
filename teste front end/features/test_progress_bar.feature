Feature: Validar a progressao da barra de carregamento

  Scenario: Validar progressao da barra
    Given que eu acesso o site "https://demoqa.com"
    When clico em start e a barra de progresso deve parar com valor menor ou igual a 25
    Then Deve clicar no botao restart depois de 100 porcento