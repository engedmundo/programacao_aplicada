from app.controle_estoque.estoque import Estoque


if __name__ == "__main__":
    estoque_fab_1 = Estoque()
    # Adicionar parafuso
    estoque_fab_1.adicionar_peca()
    estoque_fab_1.listar_estoque()
    # Adicionar Rolamento
    estoque_fab_1.adicionar_peca()
    estoque_fab_1.listar_estoque()
    estoque_fab_1.reduzir_estoque("COD01", 20)
    estoque_fab_1.listar_estoque()
    estoque_fab_1.aumentar_estoque("COD02", 10)
    estoque_fab_1.listar_estoque()





    