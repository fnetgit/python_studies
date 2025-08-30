# Introdução à List comprehension em Python

# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.


# Forma normal com loop
lista = []
for numero in range(10):
    lista.append(numero * 2)
print(lista)

# Compreensão de lista
lista = [
    numero * 2
    for numero in range(10)
]
print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    # filtro
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]

# print(novos_produtos)
print(*novos_produtos, sep='\n')
