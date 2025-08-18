import meu_modelo_matematico

print("---- Usando a importanção do módulo inteiro----")
numero = 5
print(f"O faorial de {numero} é {meu_modelo_matematico.calcular_fatorial(numero)}\n O valor de PI no nosso modulo é {meu_modelo_matematico.PI}")

from meu_modelo_matematico import eh_primo
print(f"Usando a importação de uma função especifica")

numero_teste = 17
if eh_primo(numero_teste):
    print(f"O numero {numero_teste} é primo")
else:
    print(f"O numero {numero_teste} não é primo")