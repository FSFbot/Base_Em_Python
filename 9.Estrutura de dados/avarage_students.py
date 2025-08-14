def calcular_media_estudantes(estudante):
    notas = estudante["notas"]
    if not notas:
        return 0
    media = sum(notas) / len(notas)
    return media

estudante1 = {
    "nome" : "Ana Campos",
    "Idade" : 21,
    "notas" : [8.5,9.0,7.5,10.0]    
}

estudante2 = {
    "nome" : "Lucas Nasciemento",
    "Idade": 23,
    "notas": [6.0,5.5,7.0,6.5]
}

media_Estudante1 = calcular_media_estudantes(estudante1)
print(f"A estudante {estudante1['nome']} ela tem as notas: \n {estudante1['notas']} \nlogo sua media sera igual a {media_Estudante1} ")
print(f"O estudante {estudante2['nome']} tem as notas:\n {estudante2['notas']} \n logo sua media será igual a:\n {calcular_media_estudantes(estudante2)}")

