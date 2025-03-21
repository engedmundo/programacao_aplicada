def imprime_matriz(matriz):
    for linha in matriz:
        print(linha)

consumo_mensal = [
    [27.9, 25.2, 32.6],
    [65.1, 58.8, 69.4],
    [66.9, 60.5, 71.4],
]

valor_combustivel = [
    [3.89, 4.09, 4.19],
    [2.89, 3.09, 3.19],
    [4.19, 4.29, 4.39],
]

total_gasto = []
for idx_linha in list(range(3)):
    linha = []
    for idx_coluna in list(range(3)):
        valor_gasto = consumo_mensal[idx_linha][idx_coluna] * 1000 * valor_combustivel[idx_linha][idx_coluna]

        linha.append(valor_gasto)
    
    total_gasto.append(linha)

imprime_matriz(total_gasto)

total_por_combustivel = []
for combustivel in total_gasto:
    soma_parcial = sum(combustivel)
    total_por_combustivel.append(soma_parcial)

imprime_matriz(total_por_combustivel)

soma_total = sum(total_por_combustivel)
print(soma_total)