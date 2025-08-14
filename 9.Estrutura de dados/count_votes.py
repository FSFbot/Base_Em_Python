def contar_votos(votos):
    contagem = {}
    for candidato in votos:
        contagem[candidato] = contagem.get(candidato, 0) + 1
    return contagem

lista_de_votos = [
    "Candidato A", "Candidato B", "Candidato A",
    "Candidato C", "Candidato B", "Candidato A",
    "Candidato A", "Candidato C", "Candidato B"
]

resultado_votação =  contar_votos(lista_de_votos)
print("Resultado da Votação: ")
for candidato, total_votos in resultado_votação.items():
    print(f"- {candidato} : {total_votos} votos")