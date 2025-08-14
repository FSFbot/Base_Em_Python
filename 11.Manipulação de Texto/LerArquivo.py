conteudo_exemplo = """
Olá. este é um arquivo de texto. Ele ser como exemplo para nosso exercicio. Python é uma otima ferramenta para manipulação de arquivos.
"""

with open("exemplo.txt", "w", encoding="utf-8") as f:
    f.write(conteudo_exemplo)

def analisar_arquivo(caminho_do_arquivo):
    """
    Lê um arquivo de texto e conta o número de linhas, palavras e caracteres.
    """
    try:
        with open(caminho_do_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            num_linhas = len(linhas)
            num_palavra = 0
            num_caracteres = 0
            
            for linha in linhas:
                palavras = linha.split()
                num_palavra += len(palavras)
                num_caracteres += len(linha)
                
            print(f"Analise do arquivo: {caminho_do_arquivo}\n numero de linhas: {num_linhas}\n numero de Palavras {num_palavra} \n Numeros de caracteres {num_caracteres}")
            
    except FileNotFoundError:
        print(f"Erro: O Arquivo {caminho_do_arquivo} não foi encontado.")


analisar_arquivo("exemplo.txt")