import random
import string

def gerar_senha(tamanho=12):
    if tamanho < 8:
        print("Aviso: para ser segura a senha deve ter no minimo 8 caracteres")
        tamanho = 8
        
    letras_minusculas = string.ascii_lowercase
    letras_maiusculas = string.ascii_uppercase
    digitos = string.digits
    simbolos = string.punctuation
    
    senha = [
        random.choice(letras_minusculas),
        random.choice(letras_maiusculas),
        random.choice(digitos),
        random.choice(simbolos)
    ]
    todos_caracteres = letras_minusculas + letras_maiusculas + digitos + simbolos
    for _ in range(tamanho - 4):
        senha.append(random.choice(todos_caracteres))
        
    random.shuffle(senha)
    
    return"".join(senha)

senha_gerada = gerar_senha(16)
print(f"Sua senha segura gerada será: {senha_gerada}")