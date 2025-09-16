from steps.dados import dados

def before_all(context):
    # Inicializa a classe dados antes de todos os testes
    context.dados = dados()