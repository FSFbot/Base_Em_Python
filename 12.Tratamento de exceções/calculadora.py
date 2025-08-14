def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo numero: "))
            
            operador = input("Digite um operador (+, - , * , /)")
            if operador == '+':
                resultado = num1  + num2
            elif operador == '-':
                resultado = num1 - num2
            elif operador == '*':
                resultado = num1 * num2
            elif operador == '/':
                if num2 == 0:
                    raise ZeroDivisionError
                resultado = num1 / num2
            else:
                print("Erro: Operador é invalido. tente novamente.")
                continue
        except ValueError:
            print("apenas numeros são reconhecidos para a operação")
        except ZeroDivisionError:
            print("Errp não é possível dividir por zero")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
        if input("\n Deseja fazer outro calculo? (s/n): ").lower() != 's':
            break

print("---- Calculadora Segura --------")
calculadora()
print("Calculadora encerrada")


            