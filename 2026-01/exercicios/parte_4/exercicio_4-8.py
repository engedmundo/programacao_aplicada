def informar_propriedades () -> list:
  
    quantidade_str = input ("Informe o número de materias a serem cadastrados: ") 
    quantidade = int(quantidade_str)
    propriedades = []
    for repeticao in range (quantidade):
        propriedade = {}
        nome = input("Informe o nome do Material: ")
        propriedade["nome"] = nome
        densidade_str = input("Informe a densidade do material: ")
        densidade = float(densidade_str)
        propriedade["densidade"] = densidade
        tensao_escoamento_str = input("Informe a tensao de escoamento, em MPA: ")
        tensao_escoamento = float(tensao_escoamento_str)
        propriedade["tensao_escoamento"] = tensao_escoamento
        modulo_elasticidade_str = input("Informe o modulo de elasticidade, em GPA: ")
        modulo_elasticidade = float(modulo_elasticidade_str)
        propriedade["modulo_elasticidade"] = modulo_elasticidade

        propriedades.append(propriedade)
    return propriedades


def mostrar_propriedades(propriedades: list) -> None:
    print() # Linha vazia
    cabecalho = " Material | Densidade (kg/m3) | Escoamento (MPa) | Mód. Elasticidade (GPa) "
    qtd_caracteres = len(cabecalho)
    print("=" * qtd_caracteres)
    print(cabecalho)
    print("=" * qtd_caracteres)

    for dicionario in propriedades:
        print(f" {dicionario['nome']} ", end="|")
        print(f" {dicionario['densidade']} ", end="|")
        print(f" {dicionario['tensao_escoamento']} ", end="|")
        print(f" {dicionario['modulo_elasticidade']} ", end="\n")

if __name__ == "__main__":
    propriedades = informar_propriedades()
    # print(propriedades)
    mostrar_propriedades(propriedades)
