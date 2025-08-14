def list_media():
    print("Algoritimo para cacular media de cinco numeros em uma lista")
    try:
        list = []
        for i in range(0,5):
            num = int(input("Informe um valor para ser adicionado na lista: "))
            list.append(num)
        print(f"Media desta lista é de {sum(list)/ len(list)}")
    except ValueError:
        print("Apenas numeros serão validos neste algoritimo")
        
if __name__ == "__main__":
    list_media()
    