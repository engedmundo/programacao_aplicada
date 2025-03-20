from random import randint

def gerar_matriz_quadrada(ordem):
    if ordem == 1:
        matriz = [randint(1, 10)]

    elif ordem == 2:
        # matriz = [
        #     [1, 2],
        #     [3, 4],
        # ]
        matriz = [
            [randint(1, 10), randint(1, 10)],
            [randint(1, 10), randint(1, 10)],
        ]

    elif ordem == 3:
        # matriz = [
        #     [1, 2, 3],
        #     [4, 5, 6],
        #     [7, 8, 9],
        # ]

        matriz = [
            [randint(1, 10), randint(1, 10), randint(1, 10)],
            [randint(1, 10), randint(1, 10), randint(1, 10)],
            [randint(1, 10), randint(1, 10), randint(1, 10)],
        ]