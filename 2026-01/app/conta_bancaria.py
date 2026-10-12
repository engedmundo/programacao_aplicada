from .cliente import Cliente 


class ContaBancaria: # PEP8 - convencoes, estilos e formatacao
    def __init__(
            self, 
            cliente: Cliente, 
            numero: int, 
            saldo: float = 0, # inicializando com um valor padrão. Se for informado, 
            limite: float = 0, # usa o valor informado, caso contrario, usa o valor padrao
        ) -> None:
        self.cliente = cliente
        self.numero = numero
        self.__saldo = saldo #(dunder)
        self.limite = limite

    def mostrar_dados_cliente(self) -> None:
        print("Dados do cliente:")
        print(f"Nome: {self.cliente.nome}")
        print(f"Endereço: {self.cliente.endereco}")
        print(f"CPF: {self.cliente.cpf}")
        print("##########################")

    def depositar(self, valor: float) -> None:
        self.saldo += valor

    def mostrar_saldo(self) -> None:
        print()
        print("#" * 50)
        print(f"Saldo da conta {self.numero} de {self.cliente.nome}")
        print("#" * 50)
        print()
        print(f"R$ {self.saldo:.2f}")
        print()
        print("#" * 50)

    def sacar(self, valor: float) -> bool:
        disponivel = self.saldo + self.limite
        if valor <= disponivel:
            self.saldo -= valor
            return True
        else:
            print("Operação Negada, sem saldo suficiente")
            return False

    def transferir(
            self, 
            valor: float, 
            conta_recebedor: "ContaBancaria",
        ) -> None:

        sucesso = self.sacar(valor)
        if sucesso == True:
            conta_recebedor.depositar(valor)
        else:
            print("Não foi possível efetuar a transferência")