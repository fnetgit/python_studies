# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.

def product(*args):
    result = 1
    for num in args:
        result *= num
    return result


print(product(1, 2))
print(product(2, 2, 3))


# Crie uma função que retorna se o número é par ou ímpar.

def even_or_odd(num):
    if num % 2 > 0:
        return "é ímpar."
    return "é par."


print(even_or_odd(1))
print(even_or_odd(2))
print(even_or_odd(4))
print(even_or_odd(0))
print(even_or_odd(-1))
print(even_or_odd(-2))
