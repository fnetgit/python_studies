"""
Introdução a Listas
Tipo list - Mutável
Suporta vários valores de qualquer tipo

Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
"""

print('lista 1')
lista1 = [123, True, 'Fco',  1.3, []]
lista1[-3] = 'Neto'
print(lista1)
print(lista1[2], type(lista1[4]))

print('\nlista 2')

# Alterando uma lista com índices, del, append e pop
lista2 = [1, 2, 3, 4]
lista2[2] = 55
del lista2[2]  # Remove o item e reorganiza a lista. Cuidado em listas grandes
# print(lista2)
# print(lista2[2])
lista2.append(99)
lista2.append(100)
lista2.append(10)
lista2.pop()
lista2.pop(1)
print(lista2)
lista2.clear()

print('\nlista 3')

lista3 = [9, 8, 7, 6]
lista3.insert(0, 5)  # Substitui o item do índice 0 por 5
# Cuidado, o se colocar um índice maior que o existente na lista ele adiciona no final
print(lista3)

print('\nconcatenação e extend')
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_c)
print(lista_a)
