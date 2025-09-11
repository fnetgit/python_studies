from data import numbers, fruits, products
# Nível Básico (Mapeamento e Filtros Simples)

""" 1 - Dobrar os Números:
Objetivo: Crie uma nova lista chamada doubled_numbers a partir da lista numbers, onde cada número seja multiplicado por 2.
"""


""" 2 - Extrair Preços:
Objetivo: Crie uma nova lista chamada prices contendo apenas os preços de cada dicionário na lista products."""


""" 3 - Filtrar Números Pares:
Objetivo: Crie uma nova lista chamada evens a partir da lista numbers, que contenha apenas os números que são pares.
"""


""" 4 - Frutas com a Letra 'a':
Objetivo: Crie uma nova lista chamada fruits_with_a contendo apenas as frutas da lista fruits que contenham a letra 'a'."""


# 1
doubled_numbers = [num * 2 for num in numbers]

# 2
prices = [product['preco']
          for product in products]

# 3
evens = [num
         for num in numbers
         if num % 2 == 0]

# 4
fruits_with_a = [fruit
                 for fruit in fruits
                 if 'a' in fruit]
