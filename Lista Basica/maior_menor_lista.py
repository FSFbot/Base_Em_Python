def smaller_biggest():
    print("Algoritimo para validar os maiores e menores valores dentro de uma lista")
    list = []
    qtd = int(input("Informe quantos numeros você quer que tenham na lista"))
    for i in range(0,qtd):
        num  = int(input("Informe um numero para ir para a lista"))
        list.append(num)
        
    print(f"O maior numero encontrado{max(list)} e o menor numero encontrado foi {min(list)}")
    
if __name__ == "__main__":
    smaller_biggest()
    