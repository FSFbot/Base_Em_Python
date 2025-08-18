class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade =  nacionalidade
        
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
        
    def __str__(self):
        return f"{self.titulo} por '{self.autor.nome}'"
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self._catalogo = []
    
    def adicionar_livro(self, livro):
        self._catalogo.append(livro)
        print(f"Livro {livro} adicionado com sucesso no catalogo da {self.nome}")
    def buscar_livro(self, titulo):
        for livro in self._catalogo:
            if livro.titulo.lower() == titulo.lower():
                return livro
            return None
    def emprestar_livro(self, titulo):
        livro = self.buscar_livro(titulo)
        if livro:
            if livro.disponivel:
                livro.disponivel = False
                print(f"O livro '{livro.titulo}' foi emprestado")
            else:
                print(f"Desculpe o livro {livro.titulo} ja esta emprestado.")
        else:
            print(f"Livro com titulo '{titulo} não encontrado no catálogo'")
    def mostrar_catalogo(self):
        print(f"\n---- Catalogo da {self.nome}")
        if not self._catalogo:
            print("Catalogo esta vazio.")
            return
        for livro in self._catalogo:
            status = "Disponivel" if livro.disponivel else "Emprestado"
            print(f"- {livro} | Status {status}")
        print("----------------------------------------")

# --- Demonstração de uso ---
# 1. Criar autores
autor1 = Autor("Machado de Assis", "Brasileiro")
autor2 = Autor("J.K. Rowling", "Britânica")

# 2. Criar livros, associando os autores
livro1 = Livro("Dom Casmurro", autor1)
livro2 = Livro("Harry Potter e a Pedra Filosofal", autor2)

# 3. Criar a biblioteca e adicionar os livros
biblioteca_municipal = Biblioteca("Biblioteca Municipal Central")
biblioteca_municipal.adicionar_livro(livro1)
biblioteca_municipal.adicionar_livro(livro2)

# 4. Interagir com o sistema
biblioteca_municipal.mostrar_catalogo()

print("\nRealizando empréstimos...")
biblioteca_municipal.emprestar_livro("Dom Casmurro")
biblioteca_municipal.emprestar_livro("O Pequeno Príncipe") # Livro inexistente
biblioteca_municipal.emprestar_livro("Dom Casmurro") # Tentar emprestar de novo

biblioteca_municipal.mostrar_catalogo()