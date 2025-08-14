def Fatorial():
    try:
        num = int(input("Escolha um numero para avaliarmos "))
        if num <=1:
            print("Este numero não gera fatorial")
        for i in range(2,num):
            num = num * i 
        print(num)
    except ValueError:
        print("Apenas numeros são aceitos aqui")
        
if __name__ == "__main__":
    Fatorial()