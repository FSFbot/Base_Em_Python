def capitalizar_frase():
    print("Algoritimo de capitalização de frases")
    try:
        input
        frase = input("Escolha uma frase para ser capitalizada: ")
        resp = frase.title()
        print(f"Agora podemos ver que a frase inicial é {frase}\n e a resposta que queremos{resp}")
    except ValueError:
        print("Apenas letras serão aceitas aqui")
        
if __name__ == "__main__":
    capitalizar_frase()
    
     