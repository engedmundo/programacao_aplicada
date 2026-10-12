# Entrada de dados pelo usuário:
raio_str = input("Insira o valor do raio, em mm: ")
altura_str = input("Insira o valor da altura, em mm: ")
densidade_str = input("Insira o valor da densidade do material, em g/cm3: ")
preco_str = input("Insira o valor do material, em R$/kg: ")
quantidade_str = input("Insira a quantidade de peças fabricadas: ")
# o comando input recebe os dados digitados como string

# é necessário converter de texto para número
raio = float(raio_str)
altura = float(altura_str)
densidade_g_cm = float(densidade_str)
# converter g/cm3 para kg/mm3
densidade = densidade_g_cm / 1000000
preco = float(preco_str)
quantidade = int(quantidade_str)

# calcular os dados de saída
volume_cilindro = 3.14 * (raio ** 2) * altura # area da base * altura
volume_bloco = ((2 * raio) ** 2) * altura # area da base * altura

massa_cilindro = densidade * volume_cilindro
massa_bloco = densidade * volume_bloco
massa_cavaco = densidade * (volume_bloco - volume_cilindro)

custo_mat_prima = massa_bloco * preco # 1 cilindro apenas
custo_cavaco = massa_cavaco * preco # 1 cilindro apenas
aproveitamento = (massa_cilindro / massa_bloco) * 100 # Em porcentagem
valor_total_mat_prima = custo_mat_prima * quantidade
valor_total_cavaco = custo_cavaco * quantidade

# Mostrar o resultado final
print("\n----- Resultados ------\n")
print(f"Volume do cilindro: {volume_cilindro:.2f} mm3")
print(f"Volume do bloco: {volume_bloco:.2f} mm3")
print()
print(f"Massa do cilindro: {massa_cilindro:.2f} kg")
print(f"Massa do bloco: {massa_bloco:.2f} kg")
print(f"Massa de cavaco: {massa_cavaco:.2f} kg")
print()
print(f"Custo de cavaco: R$ {custo_cavaco:.2f}")
print(f"Custo da matéria prima: R$ {custo_mat_prima:.2f}")
print()
print(f"Taxa de aproveitamento: {aproveitamento:.2f}%")
print()
print(f"Valor total Matéria-Prima: R$ {valor_total_mat_prima:.2f}")
print(f"Valor total Cavaco: R$ {valor_total_cavaco:.2f}")