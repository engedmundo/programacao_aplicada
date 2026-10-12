from random import randint


def criar_lista_aleatoria(qtd_elementos: int) -> list:
    lista = []
    for repeticao in range(qtd_elementos):
        num_aleatorio = randint(100, 150)
        lista.append(num_aleatorio)

    return lista


def calcular_media(leituras: tuple) -> float:
    soma = sum(leituras)
    qte_leituras = len(leituras)
    media = soma / qte_leituras
    return media

if __name__ == "__main__":
    lista_leituras = criar_lista_aleatoria(10)
    # converter para tupla
    leituras = tuple(lista_leituras)
    print(leituras)
    media_pressao = calcular_media(leituras)
    
    print(f"Pressão média de operação: {media_pressao:.2f} bar")

    if media_pressao > 135:
        print("A pressão está acima do ideal")
    elif media_pressao > 120:
        print("A pressão está em regime estável")
    else:
        print("A pressão está abaixo do ideal")
