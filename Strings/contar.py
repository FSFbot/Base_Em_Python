def contar_palavra(frase):
    palavras = frase.split()
    return len(palavras)

frase_exemplo = "Boto na mesa ainda mando medir"
count = contar_palavra(frase_exemplo)
print(f"A frase {frase_exemplo} tem  {count} palavras")

