"""
enumerate - enumera iteráveis (índices)
"""
# ele cria uma tupla
lista = ['A', 'B', 'C']
lista.append('D')

# Posso fazer ele começar de um número específico
# lista_enumerada = enumerate(lista, start= 13)

for item in enumerate(lista):
    print(item)
# retorna
# (0, 'A')
# (1, 'B')
# (2, 'C')
# (3, 'D')

# Desempacotando a tupla
for item in enumerate(lista):
    indices, nome = item
    print(indices, nome)
# retorna
# 0 A
# 1 B
# 2 C
# 3 D

# Faz a mesma coisa
for indices, nome in enumerate(lista):
    print(indices, nome)
