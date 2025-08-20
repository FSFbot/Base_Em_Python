def Par_Impar():
    try:
        num = int(input("Escolha um numero para podermos analisar: "))
        if num % 2 == 0:
            print(f"O numero {num} é par")
        else:
            print(f"numero {num} não é par logo é impar")
    except ValueError:
        print("Apenas numeros são aceitos")
    
    