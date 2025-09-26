# Combinations, Permutations e Product - Itertools

# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

# Utilizado quando a ORDEM NÃO IMPORTA e não há repetição de elementos. (podem ter grupos repetidos)
print_iter(combinations(pessoas, 2))
print()
# Utilizado quando a ORDEM IMPORTA e não há repetição de elementos.
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))
