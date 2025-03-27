from random import randint

numeros = [] # cria uma lista vazia

for repeticao in range(10):
    numero_aleatorio = randint(1, 10)
    numeros.append(numero_aleatorio)

print(numeros)
print(type(numeros))
tupla_numeros = tuple(numeros)
print(tupla_numeros)
print(type(tupla_numeros))

# calcular média
soma = 0
for numero in tupla_numeros:
    # soma = soma + numero
    soma += numero

qtd_numeros = len(tupla_numeros)
media = soma / qtd_numeros

print(f"Média calculada: {media:.2f}")
print(type(media))
