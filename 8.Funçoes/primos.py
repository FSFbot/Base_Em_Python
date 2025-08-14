def numeros_primos():
    print ("Algoritimo para verificar se um numero é primo ou não")
    try:
       num  = int(input("Escolha um numero para avaliarmos se é primo ou nao: \n"))
       
       if num <= 1:
           print(f"O numero {num} não é primo")
           return
       for i in range(2,num):
        if num % i == 0:
            print(f"O numero {num} não é primo (é divisivel por {i}.)")
        
            return
       print(f"numero {num} é primo")
    except ValueError:
        print("Apenas numeros são aceitos")
if __name__ == "__main__":
    numeros_primos()
    