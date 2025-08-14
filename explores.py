import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc
import polars as pl
from itertools import combinations
import networkx as nx


# Função para conectar ao SQL Server
def connect_sql_server(database=None, server="BRTLVBGS0216FU"):
    try:
        conn_str = (
            f"DRIVER={{SQL Server}};"
            f"SERVER={server};"
            f"Trusted_Connection=yes;"
        )
        if database:
            conn_str += f"DATABASE={database};"
        return pyodbc.connect(conn_str)
    except Exception as e:
        messagebox.showerror("Erro de Conexão", f"Não foi possível conectar ao servidor:\n{e}")
        raise


# Queries
query_tabelas = """
SELECT
    t.name AS tabela,
    c.name AS coluna
FROM sys.tables AS t
INNER JOIN sys.columns AS c ON t.object_id = c.object_id
ORDER BY t.name, c.column_id;
"""

query_views = """
SELECT
    v.name AS visao,
    c.name AS coluna
FROM sys.views AS v
INNER JOIN sys.columns AS c ON v.object_id = c.object_id
ORDER BY v.name, c.column_id;
"""


# Listar bancos
def listar_bancos():
    with connect_sql_server(server="BRTLVBGS0216FU") as server_conn:
        cursor = server_conn.cursor()
        cursor.execute("SELECT name FROM sys.databases WHERE database_id > 4")
        bancos = sorted(row[0] for row in cursor.fetchall())
        cursor.close()
    return bancos


# Detectar joins diretos
def detectar_joins(objetos, df_colunas):
    relacionamentos = []
    for obj1, obj2 in combinations(objetos, 2):
        cols_comuns = df_colunas.filter((pl.col("objeto") == obj1) | (pl.col("objeto") == obj2)) \
            .group_by("coluna").agg(pl.count().alias("qtd")) \
            .filter(pl.col("qtd") >= 2).select("coluna").to_series().to_list()
        for col in cols_comuns:
            relacionamentos.append([obj1, col, obj2])
    return relacionamentos


# Detectar caminhos entre tabelas
def detectar_caminhos(relacionamentos):
    G = nx.Graph()
    for origem, _, destino in relacionamentos:
        G.add_edge(origem, destino)
    caminhos = []
    for i, j in combinations(G.nodes, 2):
        try:
            path = nx.shortest_path(G, source=i, target=j)
            caminhos.append([i, j, " → ".join(path)])
        except nx.NetworkXNoPath:
            continue
    return caminhos


# Interface principal
class App(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("🔍 Explorador SQL Server")
        self.geometry("900x650")

        # Mensagem fixa de aviso
        self.aviso = tk.Label(self, text="⚠️ Certifique-se de estar conectado à VPN da empresa. (Tempo de carregamento pode variar)", fg="red")
        self.aviso.pack(pady=10)

        # Campo de endereço do servidor
        self.label_servidor = tk.Label(self, text="Servidor SQL:")
        self.label_servidor.pack(pady=5)
        self.entry_servidor = tk.Entry(self, width=50)
        self.entry_servidor.insert(0, "BRTLVBGS0216FU")  # Valor padrão
        self.entry_servidor.pack(pady=5)

        # Seletor de banco de dados
        self.label = tk.Label(self, text="Selecione um Banco:")
        self.label.pack(pady=5)
        self.combo = ttk.Combobox(self, width=50)
        self.combo.pack(pady=5)
        self.btn = tk.Button(self, text="🔍 Analisar Banco", command=self.carregar_dados)
        self.btn.pack(pady=10)
        self.status_label = tk.Label(self, text="", fg="green")
        self.status_label.pack()

        # Notebook (Abas)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True, fill='both')

        # Aba 1: Tabelas e Views
        self.aba_tabelas = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_tabelas, text="Tabelas e Views")
        self._criar_aba_tabelas()

        # Aba 2: Relacionamentos Diretos
        self.aba_relacoes = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_relacoes, text="Relações Diretas")
        self._criar_aba_relacoes()

        # Aba 3: Caminhos entre Tabelas
        self.aba_caminhos = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_caminhos, text="Caminhos entre Tabelas")
        self._criar_aba_caminhos()

        # Dados
        self.tabelas_lista = []
        self.views_lista = []
        self.objetos = []
        self.df_colunas = None
        self.relacionamentos = []
        self.caminhos = []

        # Carregar bancos
        try:
            self.bancos = listar_bancos()
            self.combo["values"] = self.bancos
        except:
            self.bancos = []

    def _criar_aba_tabelas(self):
        # Campo de busca
        self.busca_frame = tk.Frame(self.aba_tabelas)
        self.busca_frame.pack(pady=5, fill=tk.X)
        self.busca_label = tk.Label(self.busca_frame, text="Buscar Tabela/View:")
        self.busca_label.pack(side=tk.LEFT, padx=5)
        self.busca_entry = tk.Entry(self.busca_frame, width=40)
        self.busca_entry.pack(side=tk.LEFT, padx=5)
        self.busca_entry.bind("<KeyRelease>", self.filtrar_tabelas)
        self.busca_btn = tk.Button(self.busca_frame, text="Limpar", command=self.limpar_busca)
        self.busca_btn.pack(side=tk.LEFT, padx=5)

        # Lista filtrada de tabelas/views
        self.lista_frame = tk.Frame(self.aba_tabelas)
        self.lista_frame.pack(fill=tk.BOTH, expand=True)
        self.lista_scroll = tk.Scrollbar(self.lista_frame)
        self.lista_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lista_text = tk.Text(self.lista_frame, wrap=tk.WORD, yscrollcommand=self.lista_scroll.set)
        self.lista_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.lista_scroll.config(command=self.lista_text.yview)

    def _criar_aba_relacoes(self):
        # Campo de busca
        self.rela_busca_frame = tk.Frame(self.aba_relacoes)
        self.rela_busca_frame.pack(pady=5, fill=tk.X)
        self.rela_busca_label = tk.Label(self.rela_busca_frame, text="Filtrar Relações:")
        self.rela_busca_label.pack(side=tk.LEFT, padx=5)
        self.rela_busca_entry = tk.Entry(self.rela_busca_frame, width=40)
        self.rela_busca_entry.pack(side=tk.LEFT, padx=5)
        self.rela_busca_entry.bind("<KeyRelease>", self.filtrar_relacoes)
        self.rela_busca_btn = tk.Button(self.rela_busca_frame, text="Limpar", command=self.limpar_rela_busca)
        self.rela_busca_btn.pack(side=tk.LEFT, padx=5)

        # Conteúdo
        self.rela_frame = tk.Frame(self.aba_relacoes)
        self.rela_frame.pack(fill=tk.BOTH, expand=True)
        self.rela_scroll = tk.Scrollbar(self.rela_frame)
        self.rela_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.rela_text = tk.Text(self.rela_frame, wrap=tk.WORD, yscrollcommand=self.rela_scroll.set)
        self.rela_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.rela_scroll.config(command=self.rela_text.yview)

    def _criar_aba_caminhos(self):
        # Campo de busca
        self.caminho_busca_frame = tk.Frame(self.aba_caminhos)
        self.caminho_busca_frame.pack(pady=5, fill=tk.X)
        self.caminho_busca_label = tk.Label(self.caminho_busca_frame, text="Filtrar Caminhos:")
        self.caminho_busca_label.pack(side=tk.LEFT, padx=5)
        self.caminho_busca_entry = tk.Entry(self.caminho_busca_frame, width=40)
        self.caminho_busca_entry.pack(side=tk.LEFT, padx=5)
        self.caminho_busca_entry.bind("<KeyRelease>", self.filtrar_caminhos)
        self.caminho_busca_btn = tk.Button(self.caminho_busca_frame, text="Limpar", command=self.limpar_caminho_busca)
        self.caminho_busca_btn.pack(side=tk.LEFT, padx=5)

        # Conteúdo
        self.caminho_frame = tk.Frame(self.aba_caminhos)
        self.caminho_frame.pack(fill=tk.BOTH, expand=True)
        self.caminho_scroll = tk.Scrollbar(self.caminho_frame)
        self.caminho_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.caminho_text = tk.Text(self.caminho_frame, wrap=tk.WORD, yscrollcommand=self.caminho_scroll.set)
        self.caminho_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.caminho_scroll.config(command=self.caminho_text.yview)

    def carregar_dados(self):
        banco_selecionado = self.combo.get()
        if not banco_selecionado:
            messagebox.showwarning("Aviso", "Selecione um banco válido.")
            return

        servidor = self.entry_servidor.get()  # Pega o valor digitado pelo usuário

        self.status_label.config(text="🔄 Carregando dados...", fg="blue")
        self.update_idletasks()

        try:
            with connect_sql_server(banco_selecionado, server=servidor) as conn:
                df_tabelas = pl.read_database(query_tabelas, conn)
                df_views = pl.read_database(query_views, conn)

                self.tabelas_lista = sorted(df_tabelas.select("tabela").unique().to_series().to_list())
                self.views_lista = sorted(df_views.select("visao").unique().to_series().to_list())
                self.objetos = self.tabelas_lista + self.views_lista
                self.df_colunas = pl.concat([
                    df_tabelas.select(["tabela", "coluna"]).rename({"tabela": "objeto"}),
                    df_views.select(["visao", "coluna"]).rename({"visao": "objeto"})
                ])

                self.relacionamentos = detectar_joins(self.objetos, self.df_colunas)
                self.caminhos = detectar_caminhos(self.relacionamentos)

                self._mostrar_tabelas()
                self._mostrar_relacionamentos()
                self._mostrar_caminhos()

                self.status_label.config(text="✔️ Pronto!", fg="green")
        except Exception as e:
            self.status_label.config(text="❌ Erro ao carregar dados.", fg="red")
            messagebox.showerror("Erro", f"Erro ao carregar dados do banco:\n{e}")

    def _mostrar_tabelas(self, filtro=""):
        self.lista_text.delete(1.0, tk.END)
        for t in self.tabelas_lista:
            if filtro.lower() in t.lower():
                self.lista_text.insert(tk.END, f"  • {t} (Tabela)\n")
        for v in self.views_lista:
            if filtro.lower() in v.lower():
                self.lista_text.insert(tk.END, f"  • {v} (View)\n")

    def _mostrar_relacionamentos(self, filtro=""):
        self.rela_text.delete(1.0, tk.END)
        if self.relacionamentos:
            for r in self.relacionamentos:
                linha = f"{r[0]}.{r[1]} → {r[2]}.{r[1]}"
                if filtro.lower() in linha.lower():
                    self.rela_text.insert(tk.END, f"  • {linha}\n")
        else:
            self.rela_text.insert(tk.END, "  ⚠️ Nenhum relacionamento direto encontrado.")

    def _mostrar_caminhos(self, filtro=""):
        self.caminho_text.delete(1.0, tk.END)
        if self.caminhos:
            for c in self.caminhos:
                linha = f"{c[0]} → {c[2]} → {c[1]}"
                if filtro.lower() in linha.lower():
                    self.caminho_text.insert(tk.END, f"  • {c[2]}\n")
        else:
            self.caminho_text.insert(tk.END, "  ⚠️ Nenhum caminho indireto encontrado.")

    def filtrar_tabelas(self, event=None):
        termo = self.busca_entry.get()
        self._mostrar_tabelas(filtro=termo)

    def limpar_busca(self):
        self.busca_entry.delete(0, tk.END)
        self._mostrar_tabelas()

    def filtrar_relacoes(self, event=None):
        termo = self.rela_busca_entry.get()
        self._mostrar_relacionamentos(filtro=termo)

    def limpar_rela_busca(self):
        self.rela_busca_entry.delete(0, tk.END)
        self._mostrar_relacionamentos()

    def filtrar_caminhos(self, event=None):
        termo = self.caminho_busca_entry.get()
        self._mostrar_caminhos(filtro=termo)

    def limpar_caminho_busca(self):
        self.caminho_busca_entry.delete(0, tk.END)
        self._mostrar_caminhos()


# Rodar aplicação
if _name_ == "_main_":
    app = App()
    app.mainloop()