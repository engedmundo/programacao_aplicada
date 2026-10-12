import time

print("\n--- Programa para cálculo estrutural ---\n")

comprimento_inicial_str = input("Informe o comprimento inicial da viga, em metros: ")
comprimento_inicial_str = comprimento_inicial_str.replace(",", ".")
comprimento_inicial = float(comprimento_inicial_str)

temperatura_inicial_str = input("Informe a temperatura inicial, em C: ")
temperatura_inicial_str = temperatura_inicial_str.replace(",", ".")
temperatura_inicial = float(temperatura_inicial_str)

temperatura_final_str = input("Informe a temperatura final, em C: ")
temperatura_final_str = temperatura_final_str.replace(",", ".")
temperatura_final = float(temperatura_final_str)

coef_dilatacao_str = input("Informe o coeficiente de dilatação linear: m/C")
coef_dilatacao_str = coef_dilatacao_str.replace(",", ".")
coef_dilatacao = float(coef_dilatacao_str)

print("\n---- Processando ----\n")
time.sleep(3) # Aguarda 3 segundos

# Cálculos
delta_t = temperatura_final - temperatura_inicial
delta_l = comprimento_inicial * coef_dilatacao * delta_t
comprimento_final = comprimento_inicial + delta_l
comprimento_final_mm = comprimento_final * 1000
delta_l_mm = delta_l * 1000
taxa_variacao = (1 - (comprimento_inicial / comprimento_final)) * 100

# Mostrar resultado
print("\n--- Resultados ---\n")
print(f"Comprimento inicial informado: {comprimento_inicial:.2f} m")
print(f"Comprimento final: {comprimento_final_mm:.2f} mm")
print(f"Variação no comprimento: {delta_l_mm:.2f} mm")
print(f"Taxa de variação no comprimento {taxa_variacao:.2f}%")
