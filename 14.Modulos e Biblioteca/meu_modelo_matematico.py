PI = 3.141592

def calcular_fatorial(n):
    if n < 0:
        return "Erro: Número Negativo"
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n-1)

def eh_primo(n):
    if n < 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True