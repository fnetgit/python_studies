"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

names = ["Maria", "Helena", "Luiz"]

for i in range(len(names)):
    for name in names:
        if names[i] == name:
            print(i, name)

# resposta
lista = ['Maria', 'Helena', 'Luiz']

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])
