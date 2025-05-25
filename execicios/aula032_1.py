"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

user_number = input('Digite um número inteiro: ')
try:
    user_number = int(user_number)
    if user_number % 2 == 0:
        print(f'O número {user_number} é par.')
    else:
        print(f'O número {user_number} é ímpar.')
except:
    print('Não é um número inteiro.')
