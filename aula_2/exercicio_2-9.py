temp_fahrenheit_str = input("Digite a temperatura em F: ")
temp_fahrenheit = float(temp_fahrenheit_str)

temp_celsius = (temp_fahrenheit - 32) * (5/9)

print(f"Conversão: {temp_celsius} graus Celsius")