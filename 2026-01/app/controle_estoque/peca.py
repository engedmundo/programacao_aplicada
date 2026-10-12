from abc import ABC, abstractmethod

class Peca(ABC):
    def __init__(self, codigo: str, descricao: str, quantidade: int, preco: float) -> None:
        self._codigo = codigo
        self._descricao = descricao
        self._quantidade = quantidade
        self._preco = preco

    @abstractmethod
    def criar(cls):
        pass

    @abstractmethod
    def descrever(self) -> None:
        pass