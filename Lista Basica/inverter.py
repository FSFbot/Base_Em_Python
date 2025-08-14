def inverter_lista_v2():
    lista = [1, 2, 3, 4, 5, 6]
    nova_lista = []
    

    for i in range(len(lista) - 1, -1, -1):
        nova_lista.append(lista[i])
    
    print(nova_lista)

if __name__ == "__main__":
    inverter_lista_v2()
    