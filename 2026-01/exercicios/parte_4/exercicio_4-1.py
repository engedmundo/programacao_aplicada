from random import randint

def criar_matriz(ordem: int) -> list:
    matriz = []
    for i in range(ordem):
        lista = []

        for j in range(ordem):
            numero_aleatorio = randint(1, 15)
            lista.append(numero_aleatorio) # adiciona elemento no fim da lista
        
        matriz.append(lista)

    return matriz


def subtrair_matrizes(matriz_1: list, matriz_2: list) -> list:
    matriz = []
    for i, linha in enumerate(matriz_2):
        linha_resultado = []
        for j, valor in enumerate(linha):
            resultado = matriz_2[i][j] - matriz_1[i][j]
            linha_resultado.append(resultado)
            # print(f"i={i}, j={j}, valor={valor}")

        matriz.append(linha_resultado)

    return matriz

matriz_1 = criar_matriz(2)
matriz_2 = criar_matriz(2)
print(matriz_1)
print(matriz_2)

resultado = subtrair_matrizes(matriz_1, matriz_2)
print(resultado)