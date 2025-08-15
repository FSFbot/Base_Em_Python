class Pessoas:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def cumprimentar(self):
        print(f"Olá, meu nome {self.nome} e tenho {self.idade} anos")
        
class Estudante(Pessoas):
    def __init__(self, nome, idade, curso):
        super().__init__(nome,idade)
        self.curso = curso
        self.notas = []
    def adicionar_nota(self,nota):
        self.notas.append(nota)
        print(f"Nota {nota} adicionada para o estudante {self.nome}.")
    def cumprimentar(self):
        print(f"Olá, sou {self.nome}, tenho {self.idade} anos e estudo {self.curso}")
        
# --- Demonstração de uso ---
estudante1 = Estudante("Mariana", 21, "Engenharia de Software")

# O estudante pode usar o método da classe Pessoa, mas usamos a versão sobrescrita
estudante1.cumprimentar()

# Usando um método específico da classe Estudante
estudante1.adicionar_nota(9.5)
estudante1.adicionar_nota(8.0)
print(f"Notas de {estudante1.nome}: {estudante1.notas}")