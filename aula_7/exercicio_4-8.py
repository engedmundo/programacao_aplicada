produtos = {
   1: {
      "nome": "Arroz",
      "preço": 5.0, 
   },
   2: {
       "nome": "Feijão",
       "preço": 3.5,
   },
   3: {
       "nome": "Macarrão",
       "preço": 2.0,
   },
   4: {
       "nome": "Óleo",
       "preço": 7.0,
   },
   5: {
       "nome": "Sal",
       "preço": 1.5,
   },
}

compra = {
    1: 2,
    2: 1,
    3: 3,
    4: 1,
    5: 2, 
}

"""
valores_totais = {
    1: produtos[1]["preço"] * compra[1],
    2: produtos[2]["preço"] * compra[2],
    3: produtos[3]["preço"] * compra[3],
    4: produtos[4]["preço"] * compra[4],
    5: produtos[5]["preço"] * compra[5],
}
"""

# Calcular totais parciais
valores_totais = {}
total_compra = 0

for codigo, produto in produtos.items():
    preco_produto = produto["preço"] # pega valor da chave preço
    quantidade = compra[codigo]
    total_parcial =  preco_produto * quantidade
    valores_totais[codigo] = total_parcial
    total_compra += total_parcial

for codigo, produto in produtos.items():
    print(f' {codigo} | {produto["nome"]} | {produto["preço"]} | {compra[codigo]} | {valores_totais[codigo]}')

print(f"Valor final: R$ {total_compra}")
