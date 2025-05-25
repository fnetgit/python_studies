"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
try:
    hour = int(input('Digite uma hora (0-23): '))
    if hour < 0 or hour > 23:
        print('Hora inválida. Digite um número entre 0 e 23.')
    elif hour <= 11:
        print('Bom dia!')
    elif hour <= 17:
        print('Boa tarde!')
    else:
        print('Boa noite!')
except:
    print('Não é um número inteiro.')
