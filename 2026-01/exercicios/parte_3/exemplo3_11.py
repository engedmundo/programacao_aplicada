from random import choice


JOGADAS_POSSIVEIS = ["PEDRA", "PAPEL", "TESOURA"]


def solicitar_jogada_usuario() -> str:
    jogada_bruta = input("Digite sua jogada: ")
    jogada_upper = jogada_bruta.upper()
    jogada = jogada_upper.strip()

    if jogada not in JOGADAS_POSSIVEIS:
        # verdadeiro
        raise ValueError(f"Usuário informou jogada incorreta!!! {jogada}")
    else:
        # usuário jogou certo!!
        return jogada

def computador_joga() -> str:
    jogada = choice(JOGADAS_POSSIVEIS)
    return jogada


def determinar_vencedor(jogada_usuario: str, jogada_computador: str) -> str:
    # Pedra ganha de tesoura
    # Tesoura ganha de papel
    # Papel ganha de pedra
    empate = "DEU EMPATE!!!!"
    usuario = "VOCÊ VENCEU!! PARABÉNS!!"
    computador = "SE FERROU!! COMPUTADOR VENCEU!!"

    if jogada_usuario == "PEDRA" and jogada_computador == "PEDRA":
        return empate
    elif jogada_usuario == "PEDRA" and jogada_computador == "PAPEL":
        return computador
    elif jogada_usuario == "PEDRA" and jogada_computador == "TESOURA":
        return usuario
    elif jogada_usuario == "PAPEL" and jogada_computador == "PEDRA":
        return usuario
    elif jogada_usuario == "PAPEL" and jogada_computador == "PAPEL":
        return empate
    elif jogada_usuario == "PAPEL" and jogada_computador == "TESOURA":
        return computador
    elif jogada_usuario == "TESOURA" and jogada_computador == "PEDRA":
        return computador
    elif jogada_usuario == "TESOURA" and jogada_computador == "PAPEL":
        return usuario
    elif jogada_usuario == "TESOURA" and jogada_computador == "TESOURA":
        return empate
        

if __name__ == "__main__":
    # Execução do programa - Lógica de chamada das funções
    print()
    print("----- JOGO PEDRA PAPEL TESOURA -----")
    print()

    jogada_usuario = solicitar_jogada_usuario()
    jogada_computador = computador_joga()
    resultado = determinar_vencedor(jogada_usuario, jogada_computador)
    
    print("---------------- RESULTADO -------------")
    print(f"Usuário jogou: {jogada_usuario}")
    print(f"Computador jogou: {jogada_computador}")
    print("----------------------------------------")
    print(resultado)
    print("----------------------------------------")