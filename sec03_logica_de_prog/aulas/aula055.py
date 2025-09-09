# Imprecisão dos números de ponto flutuante

# Formas de corrigir:
#   Biblioteca decimal
#   Função round
#   f-string (não corrige, apenas printa)


import decimal

n1 = decimal.Decimal('0.1')
n2 = decimal.Decimal('0.7')
n3 = n1 + n2
print(n3)
print(f'{n3:.2f}')
print(round(n3, 2))
