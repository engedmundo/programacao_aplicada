nota_1 = float(input("Digite a nota 1: "))
nota_2 = float(input("Digite a nota 2: "))

media = (nota_1 + nota_2) / 2
print(f"Média {media:.2f}")

if media >= 7:
    print("Você está aprovado!!! Parabéns!!")
elif media >= 3:
    print("Você está em exame!! Estude mais!")
else:
    print(f"Você foi reprovado. Tente novamente.")
