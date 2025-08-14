agenda_telefonica = {}

def adicionar_contato(agenda,nome,telefone):
    if nome in agenda:
        print(f"Erro: O contato ja esta salvo com o nome de: {nome}")
    else:
        agenda[nome] = telefone
        print(f"Contato: {nome} adicionado com sucesso.")

def buscar_contato(agenda, nome):
    if nome in agenda:
        print(f"Contato encontrado {nome}  - Telefone: {agenda[nome]}")
    else:
        print(f"Contato {nome} não encontrado")

def editar_contato(agenda, nome, novo_telefone):
    if nome in agenda:
        agenda[nome] = novo_telefone
        print(f"Erro: Contato de {nome} atualizado para {novo_telefone}")
    else:
        print(f"Erro: Contato {nome} não encontrado para a edição")

def Remover_contato(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        print(f"Contato {nome} removido com sucesso")
    else:
        print(f"Erro: Contato {nome} não encontrado para a remoção")

# Demonstração de uso do software
      
print("--- Gerenciando Agenda Telefônica ---")
adicionar_contato(agenda_telefonica, "Maria", "9999-8888")
adicionar_contato(agenda_telefonica, "João", "7777-6666")
adicionar_contato(agenda_telefonica, "Maria", "1111-2222") # Tentando adicionar de novo
print("Agenda atual:", agenda_telefonica)

print("\n--- Buscando Contatos ---")
buscar_contato(agenda_telefonica, "João")
buscar_contato(agenda_telefonica, "Pedro")

print("\n--- Editando Contato ---")
editar_contato(agenda_telefonica, "Maria", "5555-4444")
buscar_contato(agenda_telefonica, "Maria")

print("\n--- Removendo Contato ---")
Remover_contato(agenda_telefonica, "João")
print("Agenda final:", agenda_telefonica)