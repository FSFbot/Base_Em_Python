def DecisionAge():
    print("Algoritimo para decisão da categoria da idade de uma pessoa")
    try:
        idade = int(input("Informe a sua idade para que possamos avaliar: "))
        if idade <= 12:
            print(f"Esta pessoa é uma criança com {idade} de idade")
        elif idade >= 13 and idade <=17:
            print(f"Esta pessoa é uma adolescente com {idade} de idade")
        elif idade >= 18 and idade <=59:
            print(f"Esta pessoa é um adulto com {idade} de idade")
        else:
            print(f"Esta pessoa é uma idosa com {idade} de idade")
    except ValueError:
        print("Apenas idades são aceitas!")
        
if __name__ == "__main__":
    DecisionAge()
