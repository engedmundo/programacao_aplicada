from app.disciplina import Aluno


if __name__ == "__main__":
    joao = Aluno("João", [8, 7, 6, 5, 4, 3])
    maria = Aluno("Maria", [10, 9, 8, 7, 6, 5])
    jose = Aluno("José", [5, 4, 3, 2, 1, 0])

    alunos = [joao, maria, jose]

    for aluno in alunos:
        media_aluno = aluno.calcular_media()
        aluno.mostrar_media_semestral(media_aluno)
        situacao_aluno = aluno.verificar_situacao(media_aluno)

        if situacao_aluno == "Exame":
            nota_exame_str = input("Digite a nota do exame: ")
            nota_exame = float(nota_exame_str)
            media_exame = aluno.calcular_media_exame(media_aluno, nota_exame)
            aluno.verificar_situacao_exame(media_exame)



    # media_joao = joao.calcular_media()
    # joao.mostrar_media_semestral(media_joao)
    # situcao_joao = joao.verificar_situacao(media_joao)

    # media_maria = maria.calcular_media()
    # maria.mostrar_media_semestral(media_maria)
    # situacao_maria = maria.verificar_situacao(media_maria)

    # media_jose = jose.calcular_media()
    # jose.mostrar_media_semestral(media_jose)
    # situcao_jose = jose.verificar_situacao(media_jose)