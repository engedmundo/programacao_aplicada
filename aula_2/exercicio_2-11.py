# Receber 3 variaveis A, B e C
a = float(input("Valor de A: "))
b = float(input("Valor de B: "))
c = float(input("Valor de C: "))

# trocar os valores entre A e C
# a_inicial = a
# c_inicial = c
# a = c_inicial
# c = a_inicial

# alternativa
a, c = c, a

b = c * b

print(f"A: {a}")
print(f"B: {b}")
print(f"C: {c}")

