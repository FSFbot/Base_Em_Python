def contar_vogais(palavra):
    vogais = "aeiou"
    
    contador = 0
    for letra in palavra.lower():
        if letra in vogais:
            contador += 1
    return contador

if __name__ == "__main__":
    word = "Felipe"
    numero_vogais = contar_vogais(word)
    print(f"A palavra {word} tem {numero_vogais} de vogais")
    
    
    