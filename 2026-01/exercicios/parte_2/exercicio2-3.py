# Entrada de dados pelo usuário:
potencia_str = input("Informe a potência da máquina, em kW: ")
potencia_str = potencia_str.replace(",", ".")
potencia = float(potencia_str)

qtd_horas_str = input("Informe a quantidade de horas de uso da máquina por dia: ")
qtd_horas_str = qtd_horas_str.replace(",", ".")
qtd_horas = float(qtd_horas_str)

qtd_dias_uteis_str = input("Informe a quantidade de dias úteis no mês: ")
qtd_dias_uteis_str = qtd_dias_uteis_str.replace(",", ".")
qtd_dias_uteis = int(qtd_dias_uteis_str)

preco_kwh_str = input("Informe o preço da energia por kWh: R$ ")
preco_kwh_str = preco_kwh_str.replace(",", ".")
preco_kwh = float(preco_kwh_str) # vira um comentário

# Executar os cálculos
consumo_energia_mensal = potencia * qtd_horas * qtd_dias_uteis
#                          kW          h              dias
custo_bruto = consumo_energia_mensal * preco_kwh
imposto = custo_bruto * 0.27
custo_total = custo_bruto + imposto
custo_hora_real = custo_total / (qtd_horas * qtd_dias_uteis)

# Mostrar os resultados
print("\n----- Resultados -------\n")
print(f"Consumo total de Energia: {consumo_energia_mensal:.2f} kW")
print(f"Custo bruto de Energia: R$ {custo_bruto:.2f}")
print(f"Imposto: R$ {imposto:.2f}")
print(f"Custo total: R$ {custo_total:.2f}")
print(f"Custo real por hora: R$ {custo_hora_real:.2f}")