import json

# with open("exemplo.txt", mode="r") as file:
#     conteudo = file.read()
#     print(conteudo)

# with open("outro_exemplo.txt", mode="w") as file:
#     file.write("Testando a escrita no arquivo novamente")

dados = {
    "disciplina": "Programação Aplicada",
    "professor": "Edmundo",
    "alunos": [
        {"nome": "Joel", "nota": 3.5},
        {"nome": "João", "nota": 4},
        {"nome": "Hadassa", "nota": 8}
    ]
}

# with open("programacao_aplicada.json", mode="w", encoding="utf-8") as file:
#     json.dump(dados, file, indent=4, ensure_ascii=False)


with open("programacao_aplicada.json", mode="r", encoding="utf-8") as file:
    conteudo = json.load(file)
    print(conteudo)