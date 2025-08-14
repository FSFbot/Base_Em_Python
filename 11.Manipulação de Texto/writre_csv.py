import csv
dados_csv = [
    ["Produto", "Preco", "Quantidade"],
    ["Lápis", "2.50", "50"],
    ["Caneta", "3.00", "120"],
    ["Borracha", "1.50", "75"],
    ["Caderno", "15.00", "30"]
]
with open("vendas.csv", "w", newline = "", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(dados_csv) 
    
def calcular_estatistica_vendas(caminho_csv):
    try:
        with open(caminho_csv, "r", encoding="utf-8") as f:
            leitor_csv = csv.DictReader(f)
            
            valor_total_estoque = 0
            total_de_produtos = 0
            
            print("----Processando Vendas--------")
            for linha in leitor_csv:
                preco = float(linha["Preco"])
                quantidade = int(linha["Quantidade"])
                
                valor_produto = preco * quantidade
                valor_total_estoque += valor_produto
                total_de_produtos += quantidade
                
                print(f"Produto: {linha['Produto']}, valor do Estoque : R${valor_produto:.2f}")
    except (ValueError, KeyError) as e:
        print(f"Aviso linha ignorada por erro no formato ou chave ausente: {linha} - {e}")


calcular_estatistica_vendas("vendas.csv")
