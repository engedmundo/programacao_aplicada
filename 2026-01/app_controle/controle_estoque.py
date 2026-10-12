def mostrar_estoque(estoque: dict) -> None:
    separador = "=" * 63
    cabecalho = "| Código | Nome       | Modelo     | Fabricante | Qtd | Preço |"
    print(separador)
    print(cabecalho)

    for codigo, info in estoque.items():
        print(f"| {codigo:<6}", end=" | ")
        print(f"{info['nome']:<10}", end=" | ")
        print(f"{info['modelo']:<10}", end=" | ")
        print(f"{info['fabricante']:<10}", end=" | ")
        print(f"{info['quantidade_em_estoque']:>3}", end=" | ")
        print(f"{info['preco']:>5}", end=" |\n")
    
    print(separador)


def cadastrar_peca(estoque: dict) -> dict:
    print("\n==== Cadastrando Nova Peça ====\n")
    codigo = input("Informe o código: ")
    nome = input("Informe o nome: ")
    modelo = input("Informe o modelo: ")
    fabricante = input("Informe o fabricante: ")
    quantidade_str = input("Informe a quantidade em estoque: ")
    quantidade = int(quantidade_str)
    preco_str = input("Informe o preço unitário]: ")
    preco = float(preco_str)

    print("\n==== Adicionado ao banco de dados ====\n")
    nova_peca = {
        "nome": nome,
        "modelo": modelo,
        "fabricante": fabricante,
        "quantidade_em_estoque": quantidade,
        "preco": preco
    }
    estoque[codigo] = nova_peca

    return estoque

def vender_peca(estoque: dict) -> dict:
    print("\n==== Vendendo peça do estoque ====\n")
    codigo = input("Informe o código da peça vendida: ")
    quantidade_str = input("Informe a quantidade de peças vendidas: ")
    quantidade_vendida = int(quantidade_str)

    peca = estoque[codigo]
    quantidade_estoque = peca["quantidade_em_estoque"]

    estoque_pos_venda = quantidade_estoque - quantidade_vendida

    if estoque_pos_venda < 0:
        print("Peça não pode ser vendida - sem estoque suficiente!!!")
        print(f"Quantidade desejada: {quantidade_vendida}")
        print(f"Quantidade disponível: {quantidade_estoque}")
    
    else:
        print("Venda realizada com sucesso!!!")
        # atualizar a quantidade de peças em estoque
        peca["quantidade_em_estoque"] = estoque_pos_venda
        # atualizar o registro da peça no estoque
        estoque[codigo] = peca

    return estoque

    