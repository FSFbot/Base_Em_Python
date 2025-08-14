import imaplib
import email
from email import policy
import re
import os
import tempfile
import pandas as pd
import pyodbc
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, Listbox, END, MULTIPLE


# Configurações do servidor SQL
DRIVER = '{ODBC Driver 17 for SQL Server}'
SERVER = 'BRTLVBGB0054FU'  # Prod ou homologação


def conectar_sql_server(database=None):
    conn_str = (
        f"DRIVER={DRIVER};"
        f"SERVER={SERVER};"
        "Trusted_Connection=yes;"
    )
    if database:
        conn_str += f"DATABASE={database};"
    return pyodbc.connect(conn_str)


def listar_bancos():
    """Retorna uma lista de bancos de dados do SQL Server"""
    try:
        conn = conectar_sql_server()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sys.databases WHERE database_id > 4")
        bancos = [row.name for row in cursor.fetchall()]
        conn.close()
        return bancos
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao listar bancos:\n{e}")
        return []


def baixar_anexo_do_email_imap(subject_pattern, email_user, email_pass, imap_server="imap.gmail.com"):
    """
    Busca e-mails com determinado padrão no assunto via IMAP.
    Retorna o caminho do primeiro anexo Excel encontrado.
    """
    try:
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(email_user, email_pass)
        mail.select("inbox")

        # Buscar e-mails não lidos com o padrão no assunto
        status, messages = mail.search(None, f'(UNSEEN SUBJECT "{subject_pattern}")')
        mail_ids = messages[0].split()

        if not mail_ids:
            print("[ERRO] Nenhum e-mail encontrado.")
            return None

        latest_email_id = mail_ids[-1]
        _, msg_data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email, policy=policy.default)

        print(f"[INFO] E-mail encontrado: {msg['subject']}")

        temp_dir = tempfile.gettempdir()

        # Percorrer partes do e-mail para encontrar anexos
        for part in msg.walk():
            if part.get_content_maintype() == "multipart":
                continue
            if part.get("Content-Disposition") is None:
                continue

            filename = part.get_filename()
            if filename and filename.lower().endswith((".xlsx", ".xlsm")):
                file_path = os.path.join(temp_dir, filename)
                with open(file_path, "wb") as f:
                    f.write(part.get_payload(decode=True))
                print(f"[INFO] Anexo salvo em: {file_path}")
                return file_path

        print("[ERRO] Nenhum anexo Excel encontrado.")
        return None

    except Exception as e:
        print(f"[ERRO] Erro ao acessar e-mail via IMAP: {e}")
        return None


# === Funções da interface gráfica e processamento permanecem iguais ===
# (vou manter suas funções selecionar_abas_gui, obter_nome_tabela etc.)


def selecionar_abas_gui(abas):
    selected_abas = []

    def confirmar():
        selecionadas = listbox.curselection()
        if not selecionadas:
            messagebox.showwarning("Aviso", "Nenhuma aba selecionada.")
            return
        selected_abas.extend(abas[idx] for idx in selecionadas)
        root.quit()

    tk._default_root = None
    root = tk.Tk()
    root.title("Selecione as Abas")

    tk.Label(root, text="Escolha as abas que deseja processar:", font=("Arial", 12)).pack(pady=10)

    listbox = Listbox(root, selectmode=MULTIPLE, width=50)
    listbox.pack(pady=10)

    for aba in abas:
        listbox.insert(END, aba)

    tk.Button(root, text="Confirmar", command=confirmar).pack(pady=5)

    root.mainloop()
    root.withdraw()
    root.update()

    return selected_abas


def selecionar_banco_gui(bancos):
    selected_banco = [None]

    def on_select(event):
        w = event.widget
        selection = w.curselection()
        if selection:
            idx = int(selection[0])
            selected_banco[0] = bancos[idx]

    def confirmar():
        if listbox.curselection():
            root.quit()

    tk._default_root = None
    root = tk.Tk()
    root.title("Selecione o Banco de Dados")

    tk.Label(root, text="Escolha um banco de dados:", font=("Arial", 12)).pack(pady=10)

    listbox = Listbox(root, selectmode=tk.SINGLE, width=50)
    listbox.pack(pady=10)

    for banco in bancos:
        listbox.insert(END, banco)

    listbox.bind('<<ListboxSelect>>', on_select)

    tk.Button(root, text="Confirmar", command=confirmar).pack(pady=5)

    root.mainloop()
    root.withdraw()
    root.update()

    return selected_banco[0]


def obter_linha_cabecalho(aba_nome):
    linha = simpledialog.askinteger(
        "Cabeçalho",
        f"Informe a linha de cabeçalho para a aba '{aba_nome}' (ex: 0 para primeira linha):",
        minvalue=0
    )
    return linha


def obter_nome_tabela(aba_nome, default=None):
    sugestao = default or aba_nome.replace(" ", "_")
    nome = simpledialog.askstring("Nome da Tabela", f"Digite o nome da tabela para '{aba_nome}':", initialvalue=sugestao)
    if not nome:
        raise ValueError("Nome da tabela não pode ser vazio.")
    return nome


def tabela_existe(nome_tabela, conn):
    cursor = conn.cursor()
    cursor.execute(f"IF OBJECT_ID('{nome_tabela}', 'U') IS NOT NULL SELECT 1 ELSE SELECT 0")
    result = cursor.fetchone()[0]
    return bool(result)


def criar_tabela(df, nome_tabela, conn):
    cursor = conn.cursor()

    type_map = {
        'int64': 'INT',
        'float64': 'FLOAT',
        'object': 'NVARCHAR(MAX)',
        'datetime64[ns]': 'DATETIME',
        'bool': 'BIT'
    }

    cols = []
    for col in df.columns:
        dtype = str(df[col].dtype)
        sql_type = type_map.get(dtype, 'NVARCHAR(MAX)')
        cols.append(f"[{col}] {sql_type}")

    columns_sql = ', '.join(cols)
    create_query = f"CREATE TABLE [{nome_tabela}] ({columns_sql})"
    try:
        cursor.execute(create_query)
        conn.commit()
        print(f"[INFO] Tabela '{nome_tabela}' criada com sucesso.")
    except Exception as e:
        print(f"[ERRO] Falha ao criar tabela '{nome_tabela}': {e}")
        messagebox.showerror("Erro", f"Falha ao criar tabela '{nome_tabela}':\n{e}")


def limpar_tabela(nome_tabela, conn):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM [{nome_tabela}]")
    conn.commit()


def inserir_dados(df, nome_tabela, conn):
    cursor = conn.cursor()

    if not tabela_existe(nome_tabela, conn):
        print(f"[INFO] Tabela '{nome_tabela}' não encontrada. Criando...")
        criar_tabela(df, nome_tabela, conn)

    cols = df.columns.tolist()
    escaped_cols = [f"[{col}]" for col in cols]
    placeholders = ",".join("?" * len(cols))
    insert_query = f"INSERT INTO [{nome_tabela}] ({','.join(escaped_cols)}) VALUES ({placeholders})"

    data_to_insert = [tuple(row.where(pd.notnull(row), None)) for _, row in df.iterrows()]
    try:
        cursor.executemany(insert_query, data_to_insert)
        conn.commit()
        print(f"[INFO] Dados inseridos na tabela '{nome_tabela}'.")
    except Exception as e:
        print(f"[ERRO] Erro ao inserir dados: {e}")
        messagebox.showerror("Erro", f"Erro ao inserir dados na tabela '{nome_tabela}':\n{e}")


def processar_aba(caminho_excel, aba_nome, conn):
    try:
        linha_header = obter_linha_cabecalho(aba_nome)
        df = pd.read_excel(caminho_excel, sheet_name=aba_nome, header=linha_header)
        df.dropna(how='all', inplace=True)

        nome_tabela = obter_nome_tabela(aba_nome)

        if tabela_existe(nome_tabela, conn):
            resposta = messagebox.askyesno("Tabela Existe", f"A tabela '{nome_tabela}' já existe. Deseja atualizá-la?")
            if resposta:
                limpar_tabela(nome_tabela, conn)
            else:
                print(f"[INFO] Pulando tabela '{nome_tabela}'.")
                return

        inserir_dados(df, nome_tabela, conn)
        print(f"[INFO] Tabela '{nome_tabela}' atualizada com sucesso.")

    except Exception as e:
        print(f"[ERRO] Processando aba '{aba_nome}': {e}")
        messagebox.showerror("Erro", f"Falha ao processar aba '{aba_nome}':\n{e}")


def rotina_principal():
    tk._default_root = None

    # ========== CONFIGURAÇÕES ==========
    EMAIL_USUARIO = "lucas.osilva@telefonica.com"
    EMAIL_SENHA = "Qvgzxp9g!@"
    IMAP_SERVER = "imap.outlook.com"  
    KEYWORD_ASSUNTO = "Report Capex"
    # ===================================

    # Passo 1: Buscar e-mail e obter anexo automaticamente
    caminho_excel = baixar_anexo_do_email_imap(KEYWORD_ASSUNTO, EMAIL_USUARIO, EMAIL_SENHA, IMAP_SERVER)

    if not caminho_excel:
        messagebox.showerror("Erro", "Nenhum anexo foi encontrado no e-mail.")
        return

    # Passo 2: Carregar abas do Excel
    try:
        with pd.ExcelFile(caminho_excel) as xls:
            abas = xls.sheet_names
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir o arquivo:\n{e}")
        return

    # Passo 3: Selecionar quais abas processar
    abas_selecionadas = selecionar_abas_gui(abas)
    if not abas_selecionadas:
        print("[INFO] Nenhuma aba selecionada.")
        return

    # Passo 4: Listar bancos e permitir seleção
    bancos = listar_bancos()
    if not bancos:
        messagebox.showinfo("Nenhum Banco", "Nenhum banco de dados encontrado.")
        return

    banco_selecionado = selecionar_banco_gui(bancos)
    if not banco_selecionado:
        print("[INFO] Banco de dados não selecionado.")
        return

    print(f"[INFO] Banco selecionado: {banco_selecionado}")

    # Passo 5: Conectar ao banco
    try:
        conn = conectar_sql_server(banco_selecionado)
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao conectar ao banco:\n{e}")
        return

    # Passo 6: Processar cada aba selecionada
    for aba in abas_selecionadas:
        print(f"[INFO] Processando aba: {aba}")
        processar_aba(caminho_excel, aba, conn)

    conn.close()
    print("[INFO] Rotina concluída.")


if __name__ == "__main__":
    rotina_principal()