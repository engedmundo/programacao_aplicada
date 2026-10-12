def calcular_parciais(lista_materiais: dict) -> dict:
    precos_parciais = {}

    for codigo, info_material in lista_materiais.items():
        valor_parcial = info_material["preco_unitario"] * info_material["quantidade"]
        precos_parciais[codigo] = valor_parcial

    return precos_parciais


def imprimir_relatorio(lista_materiais: dict, precos_parciais: dict) -> None:
    print("\n========================================")
    print("---- CUSTOS ESTIMADOS DO PROJETO -------")
    print("========================================")
    valor_total = 0
    
    for codigo, info_material in lista_materiais.items():
        print(f"{codigo} | {info_material['descricao']} | {info_material['quantidade']} | {info_material['preco_unitario']} | {precos_parciais[codigo]}")
        valor_total += precos_parciais[codigo]

    print(f"Valor total:              {valor_total}")
    print("========================================")



if __name__ == "__main__":
    lista_materiais = {
        "PRGAP-01": {
            "descricao": "Rolamento",
            "preco_unitario": 15,
            "quantidade": 6,        
        },
        "PRGAP-02": {
            "descricao": "Motor",
            "preco_unitario": 275,
            "quantidade": 2,
        },
        "PRGAP-03": {
            "descricao": "Sensor",
            "preco_unitario": 2.5,
            "quantidade": 30,
        },
    }

    parciais = calcular_parciais(lista_materiais)
    imprimir_relatorio(lista_materiais, parciais)