from .veiculo import Veiculo


class Aviao(Veiculo):
    def mover(self) -> None:
        print("Avião está voando")