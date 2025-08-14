def IMC():
    print("Algoritimo de calcular indice de massa corporal de uma pessoa")
    try:
        peso = float(input("Informe aqui o seu peso: \n"))
        altura = float(input("Informe aqui a sua altura: \n"))
        print(f"A pessoa que tem o peso de {peso} e altura de {altura} tera IMC de {peso/(altura*altura)}")
    except ValueError:
        print("Apenas numero são aceitos")
        
if __name__ == "__main__":
    IMC()