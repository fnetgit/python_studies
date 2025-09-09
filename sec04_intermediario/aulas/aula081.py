# Introdução à função lambda (função anônima de uma linha) e sort()/sorted()
# Útil para passar como argumento em funções como sorted(), map(), filter(), etc.

# sorted():
# É uma função built-in, funciona com qualquer iterável.
# Retorna uma nova lista ordenada, sem modificar o iterável original.

# .sort():
# É um método de lista
# Modifica a lista original em ordem crescente por padrão.
# Retorna None (não retorna uma nova lista).

# Ambos aceitam os parâmetros reverse=True e key (para ordenar com base em uma função).

# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)
lista = [
    {'nome': 'Francisco', 'sobrenome': 'Neto'},
    {'nome': 'Melissa', 'sobrenome': 'Souza'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Ely', 'sobrenome': 'Moreira'},
    {'nome': 'Ana', 'sobrenome': 'Oliveira'},
]


def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
