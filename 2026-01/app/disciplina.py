class Aluno:
    # definir atributos da classe
    def __init__(self, nome: str, notas: list[float]) -> None:
        self.nome = nome
        self.notas = notas

    def calcular_media(self) -> float:
        soma = sum(self.notas)
        quantidade = len(self.notas)
        media = soma / quantidade
        return media
    
    def mostrar_media_semestral(self, media: float) -> None:
        print(f"Aluno: {self.nome}, Média: {media}")

    def verificar_situacao(self, media: float) -> str:
        if media >= 7:
            print(f"Aluno {self.nome} está Aprovado!!")
            return "Aprovado"
        elif media >= 3:
            print(f"Aluno {self.nome} está em Exame!!")
            return "Exame"
        else: 
            print(f"Aluno {self.nome} está Reprovado!!")
            return "Reprovado"
        
    def calcular_media_exame(self, media: float, exame: float) -> float:
        media_exame = (media + exame) / 2
        return media_exame
    
    def verificar_situacao_exame(self, media_exame: int) -> None:
        if media_exame >= 5:
            print(f"Aluno {self.nome} atingiu {media_exame} e está aprovado!!")

        else:
            print(f"Aluno {self.nome} ficou com {media_exame} e está reprovado!!")
            