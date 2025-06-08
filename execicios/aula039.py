# Iterando strings com while

# *F*c*o* *N*e*t*o*

name = 'Fco Neto'
length = len(name)

count = 0
new_string = ''
while count < length:
    # new_string = new_string + '*' + name[count]
    new_string += '*' + name[count]
    count += 1
print(new_string + '*')


# Resolução
nome = 'cappuccino assassino'

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
