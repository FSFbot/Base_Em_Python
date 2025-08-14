import datetime

def log(mensagem, arquivo_log = "app.log"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H: %M: %S")
    
    mensagem_formatada = f"[{timestamp}]- {mensagem}\n"
    
    with open(arquivo_log, "a", encoding="utf-8") as f:
        f.write(mensagem_formatada)
        
        
print("Registrando eventos no arquivo 'app.log'...")
log("Aplicação iniciada.")
log("Processando dados do usuário.")
log("AVISO: Baixo espaço em disco detectado.")
log("ERRO: Falha ao conectar com o banco de dados.")
log("Aplicação finalizada.")
print("Logs registrados com sucesso.")