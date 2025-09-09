# Operadores lógicos - in (está entre) e not in (não está entre)

# Strings são iteráveis (pode navegar item por item)
#  0 1 2 3 4 5 6 7 8
#  f r a n c i s c o
#  -8-7-6-5-4-3-2-1

nome1 = 'Francisco'
print(nome1[0])  # f
print(nome1[2])  # a
print(nome1[-4])  # n

print('a' in nome1)  # True
print('cisco' in nome1)  # True
print('z' in nome1)  # False

print('-' * 8)

print('a' not in nome1)  # False
print('cisco' not in nome1)  # False
print('z' not in nome1)  # True

nome2 = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')
if encontrar in nome2:
    print(f'{encontrar} está em {nome2}')
else:
    print(f'{encontrar} não está em {nome2}')
