# Interpolação de strings com %

"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Fco'
nome2 = 'Fco'
preco = 1000.95897643
variavel = 'Sou %s, e o preço é R$ %.2f' % (nome, preco)
# Se tiver só um valor, não precisa dos parênteses
variavel2 = 'Meu nome é %s' % nome2

print(variavel)
print(variavel2)
# Coloca-se esse 0 e um numero para preencher com zeros a esquerda
print('O hexadecimal de %d é %08X' % (1500, 1500))
