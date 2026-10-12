from app_controle.manipular_arquivos import ler_arquivo, salvar_arquivo
from app_controle.controle_estoque import mostrar_estoque, cadastrar_peca, vender_peca


if __name__ == "__main__":
    caminho_arquivo = "app_controle/estoque.json"
    estoque = ler_arquivo(caminho_arquivo)
    continuar = True

    print("=" * 40)
    print("Programa de controle de estoque")
    print("=" * 40)

    while continuar == True:
        print("=" * 40)
        print("Digite a opção desejada, conforme abaixo:")
        print("1 - Consultar Estoque")
        print("2 - Cadastrar nova peça")
        print("3 - Vender peça do estoque")
        print("4 - Salvar sair do programa")
        print("=" * 40)
        opcao_usuario = input("Entre com a opção desejada: ")
        print("=" * 40)

        if opcao_usuario == "1":
            mostrar_estoque(estoque)
        elif opcao_usuario == "2":
            estoque = cadastrar_peca(estoque)
        elif opcao_usuario == "3":
            estoque = vender_peca(estoque)
        elif opcao_usuario == "4":
            continuar = False
        else:
            print("Opção inválida")

    salvar_arquivo(estoque, caminho_arquivo)