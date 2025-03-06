nota_1 = float(input("Digite a nota 1: "))
nota_2 = float(input("Digite a nota 2: "))

media = (nota_1 + nota_2) / 2
print(f"Média {media:.2f}")

if media >= 7:
    print("Você está aprovado!!! Parabéns!!")
elif media < 3:
    print("Você está reprovado! :(")
else:
    nota_exame = float(input("Digite a nota do exame: "))
    media_final = (media + nota_exame) / 2
    print(f"Média final: {media_final:.2f}")
    
    if media_final >= 5:
        print("Ufaaa!!! Está aprovado")
    else:
        print("Que pena hehehehe, Reprovado!")