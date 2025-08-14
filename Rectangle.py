def CalculateArea():
    print("Algoritimo de calculo da area de um retangulo")
    try:
        num1 = float(input("Infome um valor para a base: "))
        num2 = float(input("Informe um valor para altura: "))
        if num1 or num2 == 0:
            print("É necessario que pelo menos um dos valores seja diferente de zero")
        
        print(f"a area do retanglo sera de {num1 * num2} m^2 ")
    except ValueError:
        print("Somente numeros serão aceitos para esta operação")

if __name__ == "__main__":
    CalculateArea()