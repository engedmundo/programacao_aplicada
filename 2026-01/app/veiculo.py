from abc import ABC, abstractmethod
# Classes abstratas não podem ser diretamente instanciadas
# Ou seja, náo é possivel criar um veículo diretamente

class Veiculo(ABC):
    # ao herdar de ABC a classe veículo nao pode ser diretamente instanciada
    def __init__(self, cor: str) -> None:
        self._cor_do_veiculo = cor # encapsulamento

    # @ é um "decorator", que melhora ou dá novos comportamentos
    # a uma função

    @property
    def cor(self):
        return self._cor_do_veiculo
        # O @property diz que este método se comporta como uma variável    

    @abstractmethod
    def mover(self):
        pass
        # @abstractmethod diz que toda a classe que herdar de 
        # Veiculo precisa implementar o metodo mover 