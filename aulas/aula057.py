# Lista de listas e seus índices (iteráveis dentro de iteáveis)

salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda',  (0, 10, 20, 30, 40)],  # 2
]


print(salas[1][0])  # Elaine
print(salas[0][1])  # Helena
print(salas[2][2])  # Eduarda
print(salas[2][3][2])  # 20

print('\n')

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
