# Introdução à List comprehension

# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# ESTRUTURA 1: O FILTRO (if no final)
# Decide SE um item entra na lista.

# [ expressao_para_item_que_passou | for item in lista | if condicao_do_filtro ]

# Exemplo: [num for num in numeros if num % 2 == 0] (Pega só os números que passam no 
# filtro de "ser par").


# ESTRUTURA 2: O TRANSFORMADOR (if/else no começo)
# Decide COMO cada item entra na lista.

# [ valor_se_verdadeiro if condicao else valor_se_falso | for item in lista ]

# Exemplo: ['par' if num % 2 == 0 else 'ímpar' for num in numeros] (Todos os números 
# entram, mas transformados em "par" ou "ímpar").


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
# Transformar cada item de uma coleção em um novo item, seguindo uma regra específica, para criar uma nova coleção.

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
