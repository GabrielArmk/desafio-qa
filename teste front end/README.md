# Teste Automatizado com Selenium + Behave

Este projeto automatiza o preenchimento de um formulário no site [demoqa.com](https://demoqa.com) usando **Selenium** e **BDD** com **Behave**.

## Estrutura do projeto

teste front end/
│
├── features/
│ ├── steps/
│ │ └── test_form_steps.py # Implementação dos passos do Behave
│ ├── arq.txt # Arquivo para upload no formulário
│ └── test_form.feature # Cenário BDD em linguagem natural
│
├── requirements.txt # Pacotes Python necessários
└── README.md # Documentação

## Instalar pacotes

pip install -r requirements.txt

## Como rodar o projeto

behave

## Descrição

O teste abrirá o navegador, preencherá o formulário e validará se o modal de confirmação aparece.