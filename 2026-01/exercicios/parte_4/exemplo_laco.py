contador = 0
while contador < 50:
    resto_divisao = contador % 5
    # if resto_divisao == 0:
    #     contador +=1
    #     continue 

    if contador == 21:
        break
    print(contador)
    contador += 1

print("terminei")