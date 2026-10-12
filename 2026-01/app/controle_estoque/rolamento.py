from .peca import Peca


# Todo rolamento é uma peça - Peca é uma classe "pai" de rolamento
class Rolamento(Peca):
    def __init__(
            self, 
            codigo: str, 
            descricao: str, 
            quantidade: int, 
            preco: float,
            tipo: str,
            diametro_interno: float,
            diametro_externo: float,
            espessura: float,
        ) -> None:
        super().__init__(codigo, descricao, quantidade, preco)
        self._tipo = tipo
        self._diametro_interno = diametro_interno
        self._diametro_externo = diametro_externo
        self._espessura = espessura

    @classmethod
    def criar(cls):
        codigo = input("Informe o código da peça: ")
        descricao = input("Informe a descrição da peça: ")
        quantidade_str = input("Informe a quantidade inicial em estoque: ")
        quantidade = int(quantidade_str)
        preco_str = input("Informe o preço unitário da peça, em R$: ")
        preco = float(preco_str)
        tipo = input("Informe o tipo do rolamento: ")
        diametro_interno_str = input("Informe o diâmetro interno do rolamento, em mm: ")
        diametro_interno = float(diametro_interno_str)
        diametro_externo_str = input("Informe o diâmetro externo do rolamento, em mm: ")
        diametro_externo = float(diametro_externo_str)
        espessura_str = input("Informe a espessura do rolamento, em mm: ")
        espessura = float(espessura_str)

        rolamento = cls(
            codigo,
            descricao,
            quantidade,
            preco,
            tipo,
            diametro_interno,
            diametro_externo,
            espessura,
        )

        return rolamento
    
    def descrever(self) -> None:
        print("\n=============================================")
        print(f"Código ---------- {self._codigo}")
        print(f"Descrição ------- {self._descricao}")
        print(f"Quantidade ------ {self._quantidade} unidades")
        print(f"Preço unitário: - R$ {self._preco}")
        print(f"Tipo: ----------- {self._tipo}")
        print(f"Diâmetro Interno- {self._diametro_interno} mm")
        print(f"Diâmetro Externo- {self._diametro_externo} mm")
        print(f"Espessura ------- {self._espessura} mm")
        print("===============================================\n")