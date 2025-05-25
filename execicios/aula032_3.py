"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

name = input('Digite seu nome: ')
name_length = len(name)

if name_length == 0:
    print('Por favor, digite seu nome.')
elif name_length <= 4:
    print('Seu nome é curto.')
elif name_length <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')
