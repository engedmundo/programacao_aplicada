if __name__ == "__main__":
    print("CONTROLE DE ACESSO: ")
    pin_cadastrado = "987654"
    tentativas = 3

    while tentativas > 0:
        pin_inserido = input("Digite o código de acesso: ")
        if pin_inserido == pin_cadastrado:
            print("ACESSO PERMITIDO!")
            break

        else:
            print("ACESSO NEGADO!!!")
            tentativas = tentativas - 1
            if tentativas > 0:
                print(f"Tentativas restantes: {tentativas}")
            else:
                print("ACESSO BLOQUEADO")