from time import sleep

if __name__ == "__main__":
    print("Leituras da Caldeira")
    temperatura = 25 # temperatura inicial
    acrescimo = 2.5
    temperatura_alerta = 80
    temperatura_limite = 100

    while temperatura < temperatura_limite:
        print(f"Temperatura: {temperatura} C")
        print("Aquecendo a caldeira")
        
        if temperatura >= temperatura_alerta:
            print("ALERTA! A TEMPERATURA ESTÁ MUITO ELEVADA!!!")

        for _ in range(3):
            print(".")
            sleep(1/3)
        print()

        temperatura = temperatura + acrescimo

    print("PROCESSO DE AQUECIMENTO ENCERRADO")
    print(f"Temperatura atual: {temperatura} C")
