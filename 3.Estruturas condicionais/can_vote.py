def can_vote():
    print("Algoritimo para verificar se a pessoa ja pode votar")
    
    try:
        age = int(input("informe qual a sua idade: "))
        if age >= 16:
            print("Parabens vc ja pode votar")
        else:
            print("Neste momento você ainda nao pode votar")
    except ValueError:
        print("Apenas numero serão aceitos")
        
if __name__ == "__main__":
    can_vote()
    
    