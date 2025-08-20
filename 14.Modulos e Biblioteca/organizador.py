import os
import shutil

Pasta_a_Oragnizar = "Downloads bagunçados"
os.makedirs(Pasta_a_Oragnizar, exist_ok=True)
arquivos_exemplo = [
    "relatorio.pdf", "foto_ferias.jpg", "documento.docx",
    "planilha.xlsx", "outra_foto.jpg", "contrato.pdf", "arquivo_texto.txt"
]
for nome_arq in arquivos_exemplo:
    with open (os.path.join(Pasta_a_Oragnizar, nome_arq), "w") as f:
        f.write("conteudo exemplo")

def organizar_pasta(caminho_pasta):
    print(f"\n Iniciando organização da pasta {caminho_pasta}...")
    
    for nome_arquivo in os.listdir(caminho_pasta):
        caminho_completo  = os.path.join(caminho_pasta, nome_arquivo)
        
        if os.path.isfile(caminho_completo):
            extensao = os.path.splitext(nome_arquivo)[1].lower().replace('.', '')
            
            if extensao:
                pasta_destino = os.path.join(caminho_pasta, extensao)
                
                os.makedirs(pasta_destino, exist_ok=True)
                
                shutil.move(caminho_completo, pasta_destino)
                print(f"- Movido {nome_arquivo} para a pasta {extensao}")
    print("Organização concluida!")

organizar_pasta(Pasta_a_Oragnizar)