nota_1_str = input("Informe a nota da prova 01: ")
nota_1 = float(nota_1_str)

nota_2_str = input("Informe a nota da prova 02: ")
nota_2 = float(nota_2_str)

media = (nota_1 + nota_2) / 2

# Blocos condicionais!!!!
if media >= 7:
    print(f"Parabéns, você foi APROVADO com média {media:.2f}!!")

elif media < 3:
    print(f"Que pena, você foi REPROVADO com média {media:.2f}!!")

else:
    nota_exame_str = input("Informe a nota do exame: ")
    nota_exame = float(nota_exame_str)
    
    media_final = (media + nota_exame) / 2

    if media_final >= 5:
        print(f"Você foi aprovado com média final {media_final:.2f}.")
    
    else:
        print(f"Você foi reprovado com média final {media_final:.2f}")