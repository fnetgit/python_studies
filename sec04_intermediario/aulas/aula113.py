# reduce - faz a redução de um iterável em um valor

from functools import reduce

products = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

total_prices = reduce(
    lambda ac, p: ac + p['preco'],
    products,
    0
)
print(f'Total é {total_prices}')


print('Total:', sum([p['preco'] for p in products]))
