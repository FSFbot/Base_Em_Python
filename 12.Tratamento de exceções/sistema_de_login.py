def sistema_de_login():
    usuarios_validos = {
        "adimin": "senha123",
        "joao" : "abc123"
    }
    
    max_tentativas = 3
    
    print("--- sistema de login ---")
    
    for tentativa in range(max_tentativas, 0 , -1):
        username = input("Usuario: ")
        password = input("Senha: ")
        
        if usuarios_validos.get(username) == password:
            print("\nLogin bem sucessedido! Bem-Vindo(a)"+username+"!")
            break
        else:
            print(f"Usuario ou senha invalidos. Você tem {tentativa - 1} tentativas")
    else:
        print("\nNumero maximo de tentativas excedido. Acesso bloqueado.")

sistema_de_login()