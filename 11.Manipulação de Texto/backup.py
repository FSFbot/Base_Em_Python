import os
import shutil

os.makedirs("documentos", exist_ok= True)
with open("documentos/relatorio.txt", "w") as f:
    f.write("Este é o relatorio final")
with open("documentos/planila.xlsx", "w") as f:
    f.write("Dados da planilha")

def fazer_backup(pasta_origem, pasta_destino):
    os.makedirs(pasta_destino, exist_ok=True)
    
    print(f"Iniciando backup de {pasta_origem} para {pasta_destino}....")
    
    for nome_arquivo in os.listdir(pasta_origem):
        caminho_origem = os.path.join(pasta_origem, nome_arquivo)
        caminho_destino = os.path.join(pasta_destino, nome_arquivo)
        
        if os.path.isfile(caminho_origem):
            shutil.copy2(caminho_origem,caminho_destino)
            print(f" - Copiado {nome_arquivo}")
    print("Backup concluido com sucesso")
    
fazer_backup("documentos", "backup_documentos")