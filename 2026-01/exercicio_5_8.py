from app.carro import Carro
from app.aviao import Aviao


if __name__ == "__main__":
    fusca = Carro("azul")
    fusca.mover()
    print(fusca.cor)

    aviao = Aviao("Azul esverdeado")
    aviao.mover()
    print(aviao.cor)

    