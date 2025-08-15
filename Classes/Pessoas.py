class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        print(f"Pessoas {self.nome} Criada com sucesso!")

    def cumprimentar(self):
        print(f"Olá, meu nome ;e {self.nome} e tenho {self.idade} anos.")

    def fazer_aniversario(self):
        self.idade = self.idade+1
        print(f"Feliz aniversario ! {self.nome} agora você tem {self.idade} anos.") 
    
pessoa1 = Pessoa("Ana",30)
pessoa2 = Pessoa("Carlos", 25)


pessoa1.cumprimentar()
pessoa2.cumprimentar()

pessoa1.fazer_aniversario()