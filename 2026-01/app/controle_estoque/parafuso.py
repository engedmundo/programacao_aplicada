from .peca import Peca


# Todo parafuso é uma peça - Peca é uma classe "pai" de parafuso
# A classe "pai" é a superclasse - super
class Parafuso(Peca):
    def __init__(
            self, 
            codigo: str, 
            descricao: str, 
            quantidade: int, 
            preco: float,
            diametro: float,
            comprimento: int,
            passo: float,
        ) -> None:
        super().__init__(codigo, descricao, quantidade, preco)
        self._diametro = diametro
        self._comprimento = comprimento
        self._passo = passo

    @classmethod
    def criar(cls):
        codigo = input("Informe o código da peça: ")
        descricao = input("Informe a descrição da peça: ")
        quantidade_str = input("Informe a quantidade inicial em estoque: ")
        quantidade = int(quantidade_str)
        preco_str = input("Informe o preço unitário da peça, em R$: ")
        preco = float(preco_str)
        diametro_str = input("Informe o diâmetro do parafuso, em mm: ")
        diametro = float(diametro_str)
        comprimento_str = input("Informe o comprimento do parafuso, em mm: ")
        comprimento = int(comprimento_str)
        passo_str = input("Informe o passo do parafuso, em mm: ")
        passo = float(passo_str)

        parafuso = cls(
            codigo,
            descricao,
            quantidade,
            preco,
            diametro,
            comprimento,
            passo,
        )

        return parafuso

    def descrever(self) -> None:
        print("\n=============================================")
        print(f"Código ---------- {self._codigo}")
        print(f"Descrição ------- {self._descricao}")
        print(f"Quantidade ------ {self._quantidade} unidades")
        print(f"Preço unitário: - R$ {self._preco}")
        print(f"Diâmetro -------- {self._diametro} mm")
        print(f"Comprimento ----- {self._comprimento} mm")
        print(f"Passo ----------- {self._passo} mm")
        print("===============================================\n")