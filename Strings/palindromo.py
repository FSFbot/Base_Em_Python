def eh_palindromo(palavra):
  """
  Verifica se uma palavra é um palíndromo.
  """
  # Remove espaços e converte para minúsculas para uma comparação justa
  palavra_formatada = palavra.replace(" ", "").lower()
  # Compara a string com sua versão invertida
  return palavra_formatada == palavra_formatada[::-1]

# Exemplos de uso:
palavra1 = "arara"
if eh_palindromo(palavra1):
  print(f"A palavra '{palavra1}' é um palíndromo.")
else:
  print(f"A palavra '{palavra1}' não é um palíndromo.")

palavra2 = "python"
if eh_palindromo(palavra2):
  print(f"A palavra '{palavra2}' é um palíndromo.")
else:
  print(f"A palavra '{palavra2}' não é um palíndromo.")

# Exemplo com frase
frase = "Anotaram a data da maratona"
if eh_palindromo(frase):
    print(f"A frase '{frase}' é um palíndromo.")
else:
    print(f"A frase '{frase}' não é um palíndromo.")
     