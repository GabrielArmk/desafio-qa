import uuid

class dados():
    url_base = "https://demoqa.com"
    sufixo_unico = uuid.uuid4().hex[:8]
    nome_usuario = f"teste_{sufixo_unico}"
    senha = "Teste12345!" 
    id_user = None
    id_token = None
    livro1 = None
    livro3 = None