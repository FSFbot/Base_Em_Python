def count_pair():
    print("Algoritimo para contagem de pares de 1 a 50")
    
    soma = 0
    for i in range (1,51):
        if i % 2 == 0:
            soma = soma + 1
    print(f"Foram encontrados {soma} numeros de pares")
    
if __name__ == "__main__":
    count_pair()