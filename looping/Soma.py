def SomaNumeros():
    print("Algoritimos de soma de numeros")
    soma = 0
    for i in range(1,101):
        soma = soma + i
        print(f"a Soma ate o momento esta dando {soma}")
    

if __name__ == "__main__":
    SomaNumeros()