from cadastro import cadastra_propriedades
from tabela import imprimir_tabela

lista_prop_materiais = []

for repeticao in range(3):
    propriedades_material = cadastra_propriedades()
    lista_prop_materiais.append(propriedades_material)

imprimir_tabela(lista_prop_materiais)
