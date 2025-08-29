# Sets - Conjuntos em Python (tipo set)

# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
s1 = set('Fco')
s1 = set()  # vazio
s1 = {'Fco', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

print(3 not in s1)
for numero in s1:
    print(numero)

# Métodos úteis:
# add, update, clear, discard

s1.add('oi')  # Adiciona um único elemento
s1.update(('olá','opa'))  # Adiciona vários elementos de uma vez (cada item da tupla)
s1.update(('teste')) # Adiciona cada caractere da string separadamente: 't','e',...


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s2 = {10, 11, 12, 13}
s3 = {13, 14, 15, 16}
s4 = s2 | s3
s4 = s2 & s3
print(s4)
s4 = s2 - s3
print(s4)
s4 = s2 ^ s3
print(s4)
