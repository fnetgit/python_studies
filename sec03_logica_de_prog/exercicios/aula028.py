# Exercício de fatiamento de string

"""
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

user = input('Digite seu nome: ')
age = input('Digite sua idade: ')
if len(user) and len(age) > 0:
    print(f'Seu nome é: {user.title()}')
    print(f'Seu invertido é: {user.title()[::-1]}')
    if ' ' in user:
        print('Seu nome tem espaços')
        print(f'Seu nome tem {len(user) - user.count(' ')} letras')
    else:
        print('Seu nome não tem espaços')
        print(f'Seu nome tem {len(user)} letras')
    print(f'A primeira letra do seu nome é {user[0]}')
    print(f'A última letra do seu nome é {user[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')
