from datetime import datetime

def calcular_idade_em_dias():
    data_nasc_str = input("Digite sua data de nascimento(Formato DD/MM/AAAA): ")
    
    try:
        data_nasc = datetime.strptime(data_nasc_str,"%d/%m/%Y")
        hoje =  datetime.now()
        
        diferenca = hoje - data_nasc
        
        print("\n----Resultado-----")
        print(f"Você nasceu em  {data_nasc_strftime('%d de %B de %Y')}")
        print(f"Hoje é {hoje.strftime('%d de %B de %Y')}")
        print(f" Você ja viveu aproxidamente {diferenca.days} dias!")
    except ValueError:
        print("Erro: Formato de data invalido. Por Favor, use DD/MM/AAAA.")

calcular_idade_em_dias()