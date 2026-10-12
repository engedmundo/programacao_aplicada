from time import sleep
from datetime import datetime

inicio = datetime.now()
print(inicio)

temperatura = 500
decremento = 10
tempo_resfriamento = 0
tempo_decremento = 0.2

while temperatura >= 100:
    print(f"Temperatura atual: {temperatura} ºC")
    temperatura -= decremento
    tempo_resfriamento += tempo_decremento
    sleep(tempo_decremento)
    print(f"Tempo transcorrido: {tempo_resfriamento} seg")

fim = datetime.now()
print(fim)
tempo_execucao = fim - inicio
print(tempo_execucao)
