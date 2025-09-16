# Teste Automatizado com Selenium + Behave

Este projeto automatiza o preenchimento de um formulário no site [demoqa.com](https://demoqa.com) usando **Selenium** e **BDD** com **Behave**.

## Estrutura do projeto

Abaixo está a organização das pastas e arquivos do projeto:

- `teste_front_end/`
  - `features/`
    
    - `steps/`
      
      - `test_form_steps.py` # Implementação dos passos do Behave
        
    - `test_form.feature` # Cenário BDD em linguagem natural
      
    - `arg.txt` # Argumentos para upload no formulário
      
- `README.md` # Documentação
- `requirements.txt` # Pacotes Python necessários

## Instalar pacotes

pip install -r requirements.txt

## Como rodar o projeto

behave

## Descrição


O teste abrirá o navegador, preencherá o formulário e validará se o modal de confirmação aparece.
