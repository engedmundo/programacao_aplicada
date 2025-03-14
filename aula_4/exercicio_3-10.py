import math

def calcular_delta(a, b, c):
    delta = b ** 2 - 4 * a * c
    return delta

def calcular_uma_raiz(a, b):
    raiz = - b / (2 * a)
    return raiz

def calcular_duas_raizes(a, b, delta):
    raiz_1 = (- b + math.sqrt(delta)) / (2 * a)
    raiz_2 = (- b - math.sqrt(delta)) / (2 * a)
    return raiz_1, raiz_2


a = float(input("Digite o valor de A"))
b = float(input("Digite o valor de B"))
c = float(input("Digite o valor de C"))

# calcular delta
delta = calcular_delta(a, b, c)

if delta < 0:
    print("Não existem raízes reais")
elif delta == 0:
    print("Existe apenas uma raiz real")
    raiz = calcular_uma_raiz(a, b)
    print(f"Raiz real : {raiz:.2f}")
else:
    print("Existem duas raizes reais")
    raiz_1, raiz_2 = calcular_duas_raizes(a, b, delta)
    print(f"Raiz 1 : {raiz_1:.2f}")
    print(f"Raiz 2 : {raiz_2:.2f}")


