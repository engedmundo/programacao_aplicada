from random import randint

if __name__ == "__main__":
    posicao_sensores = list(range(1, 301, 3))
    # print(posicao_sensores)

    leituras_pressao = [
        randint(100,150) 
        for _ in posicao_sensores
    ]
    # print(leituras_pressao)
    primeiras_leituras = leituras_pressao[:10]
    ultimas_leituras = leituras_pressao[-10:]
    media_primeiras = sum(primeiras_leituras) / len(primeiras_leituras)
    media_ultimas = sum(ultimas_leituras) / len(ultimas_leituras)
    diferenca = media_ultimas - media_primeiras

    print(f"Pressão média entrada: {media_primeiras:.2f} bar")
    print(f"Pressão média saída: {media_ultimas:.2f} bar")
    print(f"Diferença entrada/saída: {diferenca:.2f} bar")
