def cadastra_propriedades():
    nome = input("Insira o nome do material: ")
    densidade = float(input("Insira a densidade, em kg/m3: "))
    mod_elasticidade = float(input("Insira o módulo de elasticidade, em GPa: "))
    escoamento = float(input("Insira a tensão de escoamento, em MPa: "))
    # criar tupla com as propriedades coletadas
    propriedades = (nome, densidade, mod_elasticidade, escoamento)
    return propriedades
