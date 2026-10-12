def solicitar_entrada(mensagem: str, tipo: str) -> float | int | str:
    entrada_str = input(f"{mensagem} ")
    
    try: # tente executar o código abaixo
        if tipo == "float":
            entrada = float(entrada_str)
        elif tipo == "int":
            entrada = int(entrada_str)
        elif tipo == "str":
            entrada = entrada_str
        else:
            # levantar um erro
            raise ValueError(f"Tipo de retorno inválido: {tipo}")
        return entrada
    
    except:
        print("Erro ao converter dados de entrada do usuário")
        print(f"Entrada do usuário: {entrada_str}, tipo: {tipo}")
        raise ValueError("Usuário digitou dados inválidos")


def identificar_material_e_custo(torque: float) -> tuple[str, int]:
    if torque < 100:
        material = "Polímero"
        custo = 50
    elif torque < 500: 
        material = "Alumínio"
        custo = 150
    else:
        material = "Aço Liga"
        custo = 300

    return material, custo

def calcular_valor_final(tipo_pagamento: str, valor: float) -> float:
    if tipo_pagamento.upper() == "PIX":
        valor_final = valor * 0.9
    elif tipo_pagamento.lower() == "crédito":
        valor_final = valor * 1.05
    else:
        raise ValueError(f"Tipo de pagamento não suportado: {tipo_pagamento}")
    
    return valor_final

def mostrar_resultado(material: str, valor_base: float, valor_final: float) -> None:
    print("\n------- Resultado --------\n")
    print(f"Material: {material}")
    print(f"Valor base: R$ {valor_base:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")
    print("-------------------------------")

if __name__ == "__main__":
    print()
    torque = solicitar_entrada("Informe o torque, em Nm:", "float")
    tipo_pagamento = solicitar_entrada("Informe o meio de pagamento (PIX ou Crédito)", "str")
    material, custo = identificar_material_e_custo(torque)
    valor_final = calcular_valor_final(tipo_pagamento, custo)
    mostrar_resultado(material, custo, valor_final)
    print()