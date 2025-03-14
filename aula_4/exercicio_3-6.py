def calcular_tensao(resistencia, corrente):
    tensao = float(resistencia) * float(corrente)
    return tensao

def calcular_resistencia(tensao, corrente):
    resistencia = float(tensao) / float(corrente)
    return resistencia

def calcular_corrente(tensao, resistencia):
    corrente = float(tensao) / float(resistencia)
    return corrente


# Ler grandezas / valores
tensao_str = input("Digite a tensão, em Volts: ")
resistencia_str = input("Digite a resistência, em Ohms: ")
corrente_str = input("Digite a corrente, em Amperes: ")

# Verificar qual das entradas é vazia
if tensao_str == "" and resistencia_str != "" and corrente_str != "":
    print("#### Calculando a tensão ####")
    tensao = calcular_tensao(corrente=corrente_str, resistencia=resistencia_str)
    print(f"Tensão calculada: {tensao:.2f} Volts")

elif resistencia_str == "" and tensao_str != "" and corrente_str != "":
    print("#### Calculando a resistencia ####")
    resistencia = calcular_resistencia(tensao_str, corrente_str)
    print(f"Resistência calculada: {resistencia:.2f} Ohms")

elif corrente_str == "" and tensao_str != "" and resistencia_str != "":
    print("#### Calculando a corrente ####")
    corrente = calcular_corrente(tensao_str, resistencia_str)
    print(f"Corrente calculada: {corrente:.2f} Amperes")


else:
    print("ERRO!!! A combinação de entrada de dados é inválida!!")


