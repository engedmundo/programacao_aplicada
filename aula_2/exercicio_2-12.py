qtd_horas = float(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o salário/hora em R$: "))

salario_bruto = qtd_horas * valor_hora
imposto = salario_bruto * 0.27
salario_liquido = salario_bruto - imposto

print(f"Salário Bruto:   R$ {salario_bruto:.2f}")
print(f"Imposto:         R$ {imposto:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")