def ler_arquivo_seguro(caminho_arquivo):
    print(f"\n  --- Tentando ler o arquivo: '{caminho_arquivo}'----")
    try:
        with open(caminho_arquivo, "r", encoding= "utf-8") as f:
            print("Arquivo aberto com sucesso. Conteúdo")
            print(f.read())
    except FileNotFoundError:
        print(f"ERRO: o arquivo no caminho '{caminho_arquivo}' não foi encontrado ")
    except PermissionError:
        print(f"Erro: Sem permissão para ler o arquivo '{caminho_arquivo}'. ")
    except Exception as e:
        print(f"ERRO inesperado ao ler o arquivo: {e}")
    finally:
        print("Finalizando a tentativa de leitura de arquivo.")


# 1. Criando um arquivo que existe para o teste de sucesso
with open("meu_arquivo.txt", "w") as f:
    f.write("Este é um arquivo de teste.")

# Teste 1: Arquivo existe e temos permissão (deve funcionar)
ler_arquivo_seguro("meu_arquivo.txt")

# Teste 2: Arquivo não existe (deve dar FileNotFoundError)
ler_arquivo_seguro("arquivo_inexistente.txt")

# Teste 3: Arquivo sem permissão (simulação)
# Em sistemas Linux/macOS, você poderia remover a permissão de leitura com:
# import os; os.chmod("meu_arquivo.txt", 0o000)
# ler_arquivo_seguro("meu_arquivo.txt")
# E depois restaurar com: os.chmod("meu_arquivo.txt", 0o644)
# Como não podemos garantir o sistema operacional, apenas deixamos o exemplo.
print("\n(Simulação de 'PermissionError' foi comentada, mas o código está pronto para tratá-lo)")