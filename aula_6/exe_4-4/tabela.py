def imprimir_tabela(propriedades_materiais):
    print("--------------|-----------------------|-----------------------------|----------------------|")
    print("-- Material --|-- Densidade (kg/m3) --|-- Mod. Elasticidade (GPa) --|-- Escoamento (MPa) --|")
    print("--------------|-----------------------|-----------------------------|----------------------|")

    for material in propriedades_materiais:
        #           nome,          densidade,  mod. elasticidade,  escoamento
        print(f" {material[0]}    | {material[1]}     | {material[2]}    | {material[3]}    |")
    
    print("--------------|-----------------------|-----------------------------|----------------------|")
