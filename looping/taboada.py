def Taboada():
    print("Algoritimo para mostrar a taboada de um numero escolhido pelo usuario")
    try:
        number = int(input("Informe um numero de qual taboada você deseja ver: "))
        print(f"O usuario escolheu a taboada do numero{number}")
        for i in range(1,11):
            print(f"{number} x {i} == {number * i}")
    except ValueError:
        print("Apenas numeros são aceitos na nossa aplicação")

if __name__ == "__main__":
    Taboada()