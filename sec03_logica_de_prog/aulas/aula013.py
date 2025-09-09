# Introduação a f-strings

nome = 'Fco'
altura = 1.60
peso = 52.0
imc = peso / (altura ** 2)

print(nome, "tem", altura, "de altura,\npesa", peso, "quilos e seu IMC é")
print(imc)

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
