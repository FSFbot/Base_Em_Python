def combinar_lista_em_dicionario(chave,valor):
    return dict(zip(chave,valor))

nomes = ["Felipe", "Williane", "Nicole", "Marcio"]
idade = [30,30,21,47]

print(f"Lista de chaves {nomes}\n lista de idades{idade}\n lista de conjuta {combinar_lista_em_dicionario(nomes,idade)}")

