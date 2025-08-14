lista_i = []

for i in range (1,101):
    lista_i.append(i)
    
lista_ii = []

for j in lista_i:
    if j % 2 != 0 :
        lista_ii.append(j)

lista_triplicada = list(map(lambda x : x * 3, lista_ii))
print(f"A principal lista {lista_i} \n e lista fica assim:\n {lista_ii}, \n Lista tripla: \n {lista_triplicada}")

