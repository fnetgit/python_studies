# Formatando strings com f-strings

"""
 s - string
 d - int
 f - float
 .<número de dígitos>f
 x ou X - Hexadecimal
 (Caractere)(><^)(quantidade)
 > - Esquerda
 < - Direita
 ^ - Centro
 = - Força o número a aparecer antes dos zeros
 Sinal - + ou - Força o sinal
 Ex.: 0>-100,.1f
 Conversion flags - !r !s !a 
 """
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{variavel:x^10}.') # Caractere de preenchimento

# Etapas da formatação (na ordem real que ocorrem):
# Ex.: print(f'{1000.4876:0=+10,.1f}')

# 1. Arredondamento → .1f  mantém 1 casa decimal
# 1000.487... vira 1000.5

# 2. Separador de milhar
# , → transforma 1000.5 em 1,000.5

# 3. Sinal
# + → adiciona + antes do número → +1,000.5

# 4. Largura total
# 0=10 → o número deve ter 10 caracteres no total
# Faltam 2 → o = diz: coloque os zeros depois do sinal

# Fica: +001,000.5
print(f'{1000.4876:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
