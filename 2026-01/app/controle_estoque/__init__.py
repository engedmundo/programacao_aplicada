"""
Exercício 5.9
Uma indústria mecânica precisa de um sistema de gerenciamento de estoque. Esse
sistema deve ser capaz de armazenar diferentes tipos de peças mecânicas, como
parafusos e rolamentos, permitindo operações de adição, remoção e consulta de estoque.
Requisitos do sistema:

Criar uma classe Peça que armazene:
Código único da peça
Descrição
Quantidade disponível no estoque
Preço
Métodos para adicionar e remover itens do estoque
Os atributos devem ser privados e acessados por métodos específicos
(Encapsulamento)

Criar classes específicas Parafuso e Rolamento, que devem herdar de Peca:
Parafuso deve possuir os atributos extras: diâmetro (mm) e comprimento (mm)
Rolamento deve possuir os atributos extras: tipo de rolamento e diâmetro externo
(mm)

Criar uma classe Estoque para armazenar as peças 
cadastradas e permitir:

Adicionar uma nova peça ao estoque

Consultar a quantidade disponível de uma peça pelo código
Listar todas as peças cadastradas
Implementar um método que possa calcular a quantidade de qualquer peça no
estoque, utilizando Polimorfismo.
Implemente o código em Python seguindo os requisitos acima. Em seguida, escreva um
código de teste que:
Cria um paraf
uso M8 (Ø8mm x 40mm) com 50 unidades e um rolamento 6004ZZ
(Ø47mm) com 20 unidades.
Adiciona essas peças ao estoque.
Exibe a quantidade disponível de cada item.
"""