def contar_frequencia_palavras(texto):
    """
    Conta a frequencia de cada palavra em uma string de texto
    """
    texto_limpo = texto.lower().replace(",","").replace("!", "").replace("?", "")
    palavras = texto_limpo.split()
    
    frequencia = {}
    
    for palavra in palavras:
        frequencia[palavra] = frequencia.get(palavra,0) + 1
    return frequencia
# Texto de exemplo
texto_exemplo = "O Python é uma linguagem de programação. A programação em Python é divertida e poderosa."

# Calcula a frequência
frequencia_das_palavras = contar_frequencia_palavras(texto_exemplo)

# Exibe o resultado
print(f"Frequência de palavras no texto:\n'{texto_exemplo}'\n")
for palavra, contagem in frequencia_das_palavras.items():
  print(f"'{palavra}': {contagem}")