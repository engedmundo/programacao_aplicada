peso = float(input("Digite o peso, em kg: "))
altura = float(input("Digite a altura, em m: "))

imc = peso / (altura ** 2)
print(f"IMC calculado: {imc:.2f}")

if imc <= 18.5:
    print("Abaixo do peso")
elif imc <= 24.9:
    print("Peso normal")
elif imc <= 29.9:
    print("Sobrepeso")
elif imc <= 34.9:
    print("Obesidade grau I")
elif imc <= 39.9:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")