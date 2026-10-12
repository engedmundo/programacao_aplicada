from .veiculo import Veiculo


class Carro(Veiculo):
    def mover(self) -> None:
        print("Carro está se movendo")