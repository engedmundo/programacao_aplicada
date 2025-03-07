from random import choice

def comparar_jogadas(usuario, computador):
    if usuario == computador:
        print("Empate")
    else:
        if usuario == "pedra" and computador == "papel":
            print("Computador ganhou!!!")
        elif usuario == "pedra" and computador == "tesoura":
            print("Usuário ganhou!!!")
        elif usuario == "papel" and computador == "pedra":
            print("Usuário ganhou!!!")
        elif usuario == "papel" and computador == "tesoura":
            print("Computador ganhou!!!")
        elif usuario == "tesoura" and computador == "pedra":
            print("Computador ganhou!!!")
        elif usuario == "tesoura" and computador == "papel":
            print("Usuário ganhou!!!")





jogadas_possiveis = ["pedra", "papel", "tesoura"]

# ler jogada usuário
jogada_usuario = input("Digite sua jogada: ")
jogada_usuario = jogada_usuario.lower()

# gerar jogada computador
jogada_computador = choice(jogadas_possiveis)
print(f"Jogada do computador: {jogada_computador}")

# comparar jogadas
comparar_jogadas(jogada_usuario, jogada_computador)