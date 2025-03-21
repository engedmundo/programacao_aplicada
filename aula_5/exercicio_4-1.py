"""
Crie um programa para gerar duas matrizes quadradas aleatórias (A e B),
no intervalo [1, 10], de mesma ordem, a qual deve ser informada pelo
usuário. 

Ao fim, o programa deve calcular e imprimir a soma entre os
elementos de A que estão abaixo da diagonal principal com os elementos
de B que estão acima da diagonal principal.
"""
# o ponto(.) antes do nome do arquivo indica que está na 
# mesma pasta
from random import randint

def gerar_matriz_quadrada(ordem):
    indices_linhas = list(range(ordem))
    indices_colunas = list(range(ordem))
    matriz = []

    for indice_linha in indices_linhas:
        linha = []
        for indice_coluna in indices_colunas:
            valor = randint(1, 10)
            linha.append(valor)
        matriz.append(linha)
        
    return matriz


def imprime_matriz(matriz):
    for linha in matriz:
        print(linha)


def soma_acima_dp(matriz):
    soma = 0
    for idx_linha, linha in enumerate(matriz):
        for idx_coluna, valor in enumerate(linha):
            if idx_coluna >= idx_linha:
                soma = soma + valor

    return soma

def soma_abaixo_dp(matriz):
    soma = 0
    for idx_linha, linha in enumerate(matriz):
        for idx_coluna, valor in enumerate(linha):
            if idx_coluna <= idx_linha:
                soma = soma + valor

    return soma


ordem = int(input("Digite a ordem das matrizes: "))

matriz_A = gerar_matriz_quadrada(ordem)
matriz_B = gerar_matriz_quadrada(ordem)

print("Matriz A:")
imprime_matriz(matriz_A)
print("Matriz B:")
imprime_matriz(matriz_B)

soma_elementos_A = soma_abaixo_dp(matriz_A)
soma_elementos_B = soma_acima_dp(matriz_B)

print(f"Soma elementos matriz A: {soma_elementos_A}")
print(f"Soma elementos matriz B: {soma_elementos_B}")
soma_final = soma_elementos_A + soma_elementos_B
print(f"Soma final: {soma_final}")
