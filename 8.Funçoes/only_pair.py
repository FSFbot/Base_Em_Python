def only_pair():
    print("Algoritimo para inlcusão de numero pares")
    try:
        lista = []
        tam = int(input("Qual o tamanho da sua lista? "))
        for i in range(1,tam+1):
            num =  int(input("Qual o numero vc deseja acrescentar a lista? "))
            if num % 2 == 0:
                lista.append(num)
        print(f"Sua lista de tamanho {tam} tem os seguintes caras \n {lista}")
    except ValueError:
        print("Apenas numero serão aceitos para a função")
        
if __name__ == "__main__":
    only_pair()
    
    