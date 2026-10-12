import json


def ler_arquivo(caminho: str) -> dict:
    with open(caminho, mode="r+", encoding="utf-8") as arquivo:
        conteudo = json.load(arquivo)

    return conteudo


def salvar_arquivo(conteudo: dict, caminho: str) -> None:
    with open(caminho, mode="w", encoding="utf-8") as arquivo:
        json.dump(conteudo, arquivo, indent=4, ensure_ascii=False)
