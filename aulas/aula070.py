"""
Retorno de valores das funções (return)
"""

# O 'return' serve para devolver um valor da função
# Sem 'return', a função retorna None por padrão


def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y

soma1 = soma(1, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(13, 20))
