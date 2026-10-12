import time

def solicitar_entrada(mensagem: str) -> float | str:
    entrada_str = input(mensagem).strip() # Strip - remove espaços em branco no começo e no fim do texto.
    # verificar se valor de entrada é nulo ou vazio
    if entrada_str == "":
        return entrada_str
    
    try:
        entrada = float(entrada_str)
        return entrada
    
    except:
        raise ValueError("Dados informados são inválidos!!!")


def calcular_tensao(resistencia: float, corrente: float) -> float:
    tensao = resistencia * corrente
    return tensao


def calcular_resistencia(tensao: float, corrente: float) -> float:
    resistencia = tensao / corrente
    return resistencia


def calcular_corrente(tensao: float, resistencia: float) -> float:
    corrente = tensao / resistencia
    return corrente


def processar_dados(tensao: float, resistencia: float, corrente: float) -> tuple[float, str]:
    if tensao == "" and resistencia != "" and corrente != "":
        resultado = calcular_tensao(resistencia, corrente)
        return resultado, "Volts"
    elif resistencia == "" and tensao != "" and corrente != "":
        resultado = calcular_resistencia(tensao, corrente)
        return resultado, "Ohms"
    elif corrente == "" and tensao != "" and resistencia != "":
        resultado = calcular_corrente(tensao, resistencia)
        return resultado, "Amperes"
    else:
        raise ValueError("Não foi possível identificar o valor a ser calculado!")


if __name__ == "__main__":
    # Execução do programa - Lógica de chamada das funções
    print()
    print("Informe os valores de cálculo. Se a variável solicitada é o valor desejado, apenas tecle Enter.")
    print()
    resistencia = solicitar_entrada("Informe a resistência, em Ohms: ")
    tensao = solicitar_entrada("Informe o valor da tensao, em Volts: ")
    corrente = solicitar_entrada("Informe o valor da corrente, em Amperes: ")
    print()
    # simulando um cálculo muito complexo.....
    print("Calculando...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    print()

    # Calcular os dados
    resultado, unidade = processar_dados(tensao, resistencia, corrente)

    # Mostrar o resultado
    print(f"O resultado é: {resultado:.2f} {unidade}")

