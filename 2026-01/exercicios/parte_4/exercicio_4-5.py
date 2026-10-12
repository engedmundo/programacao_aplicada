from faker import Faker
from random import randint


def criar_operador(id: int) -> tuple[int, str]:
    faker = Faker("pt-BR")
    nome_operador = faker.name()
    operador = (id, nome_operador)
    return operador


def criar_conjunto_especialistas(quantidade: int, operadores: list) -> set:
    conjunto = set()
    quantidade_operadores = len(operadores) - 1

    while len(conjunto) < quantidade:
        indice = randint(0, quantidade_operadores)
        operador = operadores[indice]
        conjunto.add(operador)

    return conjunto

def imprimir_relatorio(titulo: str, operadores: list) -> None:
    print("\n================================================")
    print(f"---- {titulo} -----")
    print("================================================")

    for id, nome in operadores:
        print(f"ID: {id} | {nome}")

    print("================================================")


if __name__ == "__main__":
    # criar nomes e ids
    lista_ids = list(range(1, 13))
    
    operadores = []
    for id in lista_ids:
        operador = criar_operador(id)
        operadores.append(operador)

    operadores_torno = criar_conjunto_especialistas(8, operadores)
    operadores_fresa = criar_conjunto_especialistas(6, operadores)

    polivalentes = operadores_torno.intersection(operadores_fresa)

    especialistas_torno = operadores_torno - operadores_fresa
    especialistas_fresa = operadores_fresa - operadores_torno

    imprimir_relatorio("TODOS OS OPERADORES", operadores)
    imprimir_relatorio("OPERADORES POLIVALENTES", polivalentes)
    imprimir_relatorio("OEPRADORES DE TORNO", especialistas_torno)
    imprimir_relatorio("OEPRADORES DE FRESA", especialistas_fresa)