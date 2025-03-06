valor = float(input("Digite o valor do produto: "))
estado = input("Digite a sigla do estado: ")

erro = False

if estado == "MG":
    taxa = 0.07
elif estado == "SP":
    taxa = 0.12
elif estado == "RJ":
    taxa = 0.15
elif estado == "MS":
    taxa = 0.08
else:
    erro = True

if erro == True:
    print("ERRO! Estado digitado é inválido")
else:
    imposto = valor * taxa
    valor_final = valor + imposto
    print(f"Valor final do produto: R$ {valor_final:.2f}")
