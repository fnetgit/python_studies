# Nível Avançado (Listas Aninhadas e Lógica Complexa)

""" "Achatamento" de Matriz (Flatten):
Objetivo: Crie uma lista única chamada flattened_list a partir da matriz, contendo todos os números. 
"""


""" Tabela de Multiplicação:
Objetivo: Crie uma lista de tuplas chamada multiplication_table_of_3, onde cada tupla contém uma multiplicação da tabuada do 3, de 1 a 10. Ex: (3, 'x', 1, '=', 3).

Resultado esperado:

[
    (3, 'x', 1, '=', 3),
    (3, 'x', 2, '=', 6),
    ...
    (3, 'x', 10, '=', 30)
] """

import pprint
from data import matrix
flattened_list = [num
                  for list in matrix for num in list]


multiplication_table_of_3 = [(3, 'x', num, '=', num*3)
                             for num in range(1, 11)]
pprint.pprint(multiplication_table_of_3)
