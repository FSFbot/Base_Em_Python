def Info():
    print("Algoritimo de Recolher informaçoes e orgaqnizar")
    
    name = input("Informe qual o seu nome: ")
    age = int(input("Informe a sua idade: "))
    height = float(input("Informe sua altura: "))
    
    print(f"O usuario de nome {name}, possui a idade de {age} com a altura de {height}")
    
if __name__ == "__main__":
    Info()
    