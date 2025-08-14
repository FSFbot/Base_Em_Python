def par_impar():
    print("Algoritmo de avalição se um numero é par ou impar")
    try:
        num = int(input("Informe um numero e ele sera avaliado: "))
        if num % 2 == 0:
            print(f"{num} é um par")
        else:
            print(f"{num} é impar")
    except ValueError:
        print("Apenas numeros são aceitos aqui")
if __name__ == "__main__":
    par_impar()
    
    