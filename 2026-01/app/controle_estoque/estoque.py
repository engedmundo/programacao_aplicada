from .peca import Peca
from .parafuso import Parafuso
from .rolamento import Rolamento


class Estoque:
    def __init__(self, pecas: list[Peca] = []) -> None:
        self._pecas = pecas

    def adicionar_peca(self) -> None:
        tipo_de_peca = input("Informe o tipo de peca que deseja incluir: ")
        if tipo_de_peca == "PARAFUSO":
            peca = Parafuso.criar()
            self._pecas.append(peca)

        elif tipo_de_peca == "ROLAMENTO":
            peca = Rolamento.criar()
            self._pecas.append(peca)
        
        else:
            print("Peça não permitida para o estoque!!")

    def listar_estoque(self) -> None:
        print("\n--- LISTAGEM DE ESTOQUE ---\n")
        for peca in self._pecas:
            peca.descrever()

    def reduzir_estoque(self, codigo: str, quantidade: int) -> None:
        peca_encontrada = False
        for peca in self._pecas:
            if peca._codigo == codigo:
                peca._quantidade -= quantidade
                peca_encontrada = True

        if peca_encontrada == True:
            print(f"Estoque da peça {codigo} reduzido em {quantidade} unidades")
        else:
            print(f"Peça não encontrada!!")

    def aumentar_estoque(self, codigo: str, quantidade: int) -> None:
        peca_encontrada = False
        for peca in self._pecas:
            if peca._codigo == codigo:
                peca._quantidade += quantidade
                peca_encontrada = True

        if peca_encontrada == True:
            print(f"Estoque da peça {codigo} aumentado em {quantidade} unidades")
        else:
            print(f"Peça não encontrada!!")