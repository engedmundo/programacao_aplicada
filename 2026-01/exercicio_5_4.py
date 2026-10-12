from app.cliente import Cliente
from app.conta_bancaria import ContaBancaria


if __name__ == "__main__":
    joao = Cliente(
        "João da Silva",
        "Av. Brasil, 100, Apto 201, Passo Fundo",
        "123.456.789-00",
        )
    conta_joao = ContaBancaria(
        joao,
        14455,
        32,
        50,
    )

    # conta_joao.mostrar_dados_cliente()
    conta_joao.mostrar_saldo()
    conta_joao.depositar(3000)
    conta_joao.mostrar_saldo()
    conta_joao.sacar(5000)
    conta_joao.sacar(300)
    conta_joao.mostrar_saldo()

    maria = Cliente(
        "Maria da Silva",
        "Av Presidente Vargas, 200, Casa",
        "987.654.321-11",
    )
    conta_maria = ContaBancaria(
        maria,
        998877,
    )
    conta_maria.depositar(1000)
    conta_maria.mostrar_saldo()
    conta_maria.transferir(500, conta_joao)
    conta_maria.mostrar_saldo()
    conta_joao.mostrar_saldo()

    conta_joao.__saldo = 10000000000000000
    conta_joao.mostrar_saldo()