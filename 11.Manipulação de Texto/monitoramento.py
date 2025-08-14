import os
import time

config_file = "config.ini"
with open (config_file, "w") as f:
    f.write("[config]\nuser = admin")

def monitorar_arquivos(caminho_do_arquivo, intervalo_segundos=5):
    try:
        ultimo_tempo_modificado = os.path.getatime(caminho_do_arquivo)
        print(f"Monitorando o arquivo '{caminho_do_arquivo}'. Precione Ctrl+c para parar.")
        print(f"Estado inicial registrado. Altere o arquivo para ver a detecção.")
        while True:
            time.sleep(intervalo_segundos)
            tempo_atual_modificado = os.path.getatime(caminho_do_arquivo)
            
            if tempo_atual_modificado != ultimo_tempo_modificado:
                print(f"\n! ALERTA: O arquivo {caminho_do_arquivo} foi modificado")
                print("-> Recarregando configurações...")
                
                with open(caminho_do_arquivo, "r") as f:
                    print(f"Novo conteudo:\n ---\n{f.read().strip()}\n ---\n")
                    
                ultimo_tempo_modificado = tempo_atual_modificado
    except FileNotFoundError:
        print(F"Erro: O arquivo {caminho_do_arquivo} não foi encontrado")
    except KeyboardInterrupt:
        print("\nMonitoramento interrompido pelo usuario.")