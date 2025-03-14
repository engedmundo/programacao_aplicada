# Escreva um programa que solicite ao usuário a estatura de 3 pessoas. Ao
# fim, o programa deve imprimir as estaturas em ordem crescente.
estatura_1 = float(input("Digite a estatura 1, em metros: "))
estatura_2 = float(input("Digite a estatura 2, em metros: "))
estatura_3 = float(input("Digite a estatura 3, em metros: "))

if estatura_1 <= estatura_2 and estatura_1 <= estatura_3:
    print(f"A menor estatura: {estatura_1} m")

    if estatura_2 <= estatura_3:
        print(f"Segunda menor estatura: {estatura_2} m")
        print(f"A maior estatura é: {estatura_3} m")
    else:
        print(f"Segunda menor estatura: {estatura_3} m")
        print(f"A maior estatura é: {estatura_2} m")

elif estatura_2 <= estatura_1 and estatura_2 <= estatura_3:
    print(f"A menor estatura: {estatura_2} m")

    if estatura_1 <= estatura_3:
        print(f"Segunda menor estatura: {estatura_1} m")
        print(f"A maior estatura é: {estatura_3} m")
    else:
        print(f"Segunda menor estatura: {estatura_3} m")
        print(f"A maior estatura é: {estatura_1} m")

elif estatura_3 <= estatura_1 and estatura_3 <= estatura_2:
    print(f"A menor estatura: {estatura_3} m")

    if estatura_1 <= estatura_2:
        print(f"Segunda menor estatura: {estatura_1} m")
        print(f"A maior estatura é: {estatura_2} m")
    else:
        print(f"Segunda menor estatura: {estatura_2} m")
        print(f"A maior estatura é: {estatura_1} m")

