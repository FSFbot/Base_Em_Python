numeros = [10, 15, 20, 25, 30, 35, 40, 45, 50]

# Passo 1: Filtrar apenas os números ímpares da lista.
# Usamos uma função lambda (função anônima) para definir a condição de filtro.
# A condição x % 2 != 0 é verdadeira para números ímpares.
numeros_impares = filter(lambda x: x % 2 != 0, numeros)

# O resultado de filter() é um iterador, então convertemos para lista para visualizar
numeros_impares_lista = list(numeros_impares)
print(f"Lista original: {numeros}")
print(f"1. Apenas os números ímpares (usando filter): {numeros_impares_lista}")


# Passo 2: Pegar a lista filtrada e calcular o dobro de cada número.
# Usamos map() para aplicar a função lambda que multiplica por 2.
dobro_dos_impares = map(lambda x: x * 2, numeros_impares_lista)

# O resultado de map() também é um iterador. Convertemos para lista.
resultado_final = list(dobro_dos_impares)
print(f"2. O dobro dos ímpares (usando map): {resultado_final}")